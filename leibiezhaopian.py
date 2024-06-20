from datetime import datetime
import shutil
from flask import Flask, request, jsonify, send_from_directory
from flask_mysqldb import MySQL
import os
from flask_cors import CORS
from classification import process_image_detection
from classification import translate_object_list
from generate import create_variation

app = Flask(__name__)
CORS(app)  # 启用 CORS，允许所有来源的请求
mysql = MySQL(app)

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'photo_management'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['UPLOAD_FOLDER'] = 'uploads\\'
app.config['UPLOAD_FOLD'] = 'static/upload/temp'
app.config['GENERATED_FOLDER'] = 'static/upload/generated'

if not os.path.exists(app.config['UPLOAD_FOLD']):
    os.makedirs(app.config['UPLOAD_FOLD'])

if not os.path.exists(app.config['GENERATED_FOLDER']):
    os.makedirs(app.config['GENERATED_FOLDER'])

@app.route('/upload_temp', methods=['POST'])
def upload_temp():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.jpg'):
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLD'], filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully', 'path': file_path}), 200

    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/generate_image', methods=['POST'])
def generate_image():
    data = request.get_json()
    username = data.get('username')
    category = data.get('category')
    image_name = data.get('imageName')
    file_path = data.get('filePath')

    if not all([username, category, image_name, file_path]):
        return jsonify({'success': False, 'message': 'Missing data'}), 400

    # 检查用户是否存在
    cur = mysql.connection.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if not user:
        return jsonify({'success': False, 'message': 'User not found'}), 404
    user_id = user['id']

    # 检查类别是否存在
    cur.execute("SELECT id FROM categories WHERE user_id = %s AND name = %s", (user_id, category))
    category_row = cur.fetchone()

    if not category_row:
        # 如果类别不存在，创建新类别
        cur.execute("INSERT INTO categories (user_id, name) VALUES (%s, %s)", (user_id, category))
        mysql.connection.commit()
        cur.execute("SELECT id FROM categories WHERE user_id = %s AND name = %s", (user_id, category))
        category_row = cur.fetchone()

    category_id = category_row['id']

    # 生成图像的保存路径
    user_folder = os.path.join(app.config['GENERATED_FOLDER'], username)
    category_folder = os.path.join(user_folder, category)
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

    file_extension = os.path.splitext(file_path)[1]
    new_filename = f"{username}_{category}_{image_name}{file_extension}"
    new_file_path = os.path.join(category_folder, new_filename)

    generated_image_path = create_variation(image_path=file_path, output_dir=new_file_path)

    # 将图像信息存储到数据库
    cur.execute("INSERT INTO photos (title, category_id, file_path) VALUES (%s, %s, %s)",
                (image_name, category_id, new_file_path))
    mysql.connection.commit()
    cur.close()

    return jsonify({'success': True, 'message': 'Image generated successfully', 'path': generated_image_path}), 200

# 照片上传页面的类别选择：根据用户id做展示
@app.route('/select_categories', methods=['GET'])
def get_categories():
    username = request.args.get('username')
    
    if not username:
        return jsonify({'error': '需要提供用户名'}), 400
    
    cur = mysql.connection.cursor()

    # 首先通过用户名查找用户ID
    user_query = "SELECT id FROM users WHERE username = %s"
    cur.execute(user_query, (username,))
    user = cur.fetchone()

    if not user:
        cur.close()
        return jsonify({'error': '用户不存在'}), 400

    userid = user['id']

    # 使用用户ID查找分类
    categories_query = """
        SELECT id, name 
        FROM categories 
        WHERE user_id = %s
    """
    cur.execute(categories_query, (userid,))
    categories = cur.fetchall()
    cur.close()

    categories_list = [{'id': category['id'], 'name': category['name']} for category in categories]

    return jsonify(categories_list), 200

# 照片上传页面的照片上传：需要用户id和类别id
@app.route('/upload_photos', methods=['POST'])
def upload_photos():
    username = request.form['username']
    title = request.form['title']
    category_id = request.form['category_id']
    photo = request.files['file']

    if not photo:
        return jsonify({'error': '文件不存在'}), 400

    cur = mysql.connection.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if not user:
        return jsonify({'message': '用户不存在'}), 400
    user_id = user['id']

    current_dir = 'static/upload/'
    file_extension = os.path.splitext(photo.filename)[1]

    if category_id == 'auto':
        cur.execute("SELECT id, name FROM categories WHERE user_id = %s", (user_id,))
        categories = cur.fetchall()
        if not categories:
            return jsonify({'message': '没有可用的类别'}), 400

        category_names = [category['name'] for category in categories]
        translation_mapping = translate_object_list(category_names)

        temp_dir = 'static/upload/temp'
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        
        temp_filename = f"{username}_{title}_temp{file_extension}"
        temp_path = os.path.join(temp_dir, temp_filename)
        photo.save(temp_path)

        best_match = process_image_detection(temp_path, translation_mapping)
        category_name = best_match[0]

        # Debug information
        print(f"user_id: {user_id}, category_name: {category_name}")

        cur.execute("SELECT id FROM categories WHERE user_id = %s AND name = %s", (user_id, category_name))
        category = cur.fetchone()

        if not category:
            # 如果没有找到匹配的类别，检查是否存在名为 "其他" 的类别
            cur.execute("SELECT id FROM categories WHERE user_id = %s AND name = %s", (user_id, '其他'))
            other_category = cur.fetchone()

            if not other_category:
                # 如果 "其他" 类别不存在，则创建一个新的 "其他" 类别
                cur.execute("INSERT INTO categories (name, user_id) VALUES (%s, %s)", ('其他', user_id))
                mysql.connection.commit()
                cur.execute("SELECT id FROM categories WHERE user_id = %s AND name = %s", (user_id, '其他'))
                other_category = cur.fetchone()

            category_id = other_category['id']
            category_name = '其他'
        else:
            category_id = category['id']

        final_dir = os.path.join(current_dir, username, category_name)
        if not os.path.exists(final_dir):
            os.makedirs(final_dir)

        new_filename = f"{username}_{category_name}_{title}{file_extension}"
        final_path = os.path.join(final_dir, new_filename)

        # Debug information
        print(f"Moving file from {temp_path} to {final_path}")

        try:
            shutil.move(temp_path, final_path)
            print(f"File moved to: {final_path}")
        except Exception as e:
            print(f"Error moving file: {e}")
            return jsonify({'message': '文件迁移失败'}), 500

    else:
        cur.execute("SELECT name FROM categories WHERE id = %s AND user_id = %s", (category_id, user_id))
        category = cur.fetchone()
        if not category:
            return jsonify({'message': '该类别未创建'}), 400

        category_name = category['name']
        final_dir = os.path.join(current_dir, username, category_name)
        if not os.path.exists(final_dir):
            os.makedirs(final_dir)

        new_filename = f"{username}_{category_name}_{title}{file_extension}"
        final_path = os.path.join(final_dir, new_filename)

        # Debug information
        print(f"Saving file to: {final_path}")

        try:
            photo.save(final_path)
            print(f"File saved to: {final_path}")
        except Exception as e:
            print(f"Error saving file: {e}")
            return jsonify({'message': '文件保存失败'}), 500

    cur.execute("INSERT INTO photos (title, category_id, file_path) VALUES (%s, %s, %s)", 
                (title, category_id, final_path))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': '上传成功', 'path': final_path, 'category_name': category_name}), 200

# 相册展示页面的后端：根据用户id展示相册
@app.route('/xiangce', methods=['GET'])
def get_album():
    username = request.args.get('username')
    print(username)
    
    if not username:
        return jsonify({'message': '用户名不能为空'}), 400

    cursor = mysql.connection.cursor()

    # 获取用户ID
    query_user = "SELECT id FROM users WHERE username = %s"
    cursor.execute(query_user, (username,))
    user = cursor.fetchone()

    if not user:
        return jsonify({'message': '用户不存在'}), 400

    user_id = user['id']
    print("user_id",user_id)

    # 获取用户的所有类别
    query_categories = """
    SELECT id, name
    FROM categories
    WHERE user_id = %s
    """
    cursor.execute(query_categories, (user_id,))
    categories = cursor.fetchall()

    # 获取每个类别的最新图片路径
    for category in categories:
        query_photos = """
        SELECT file_path
        FROM photos
        WHERE category_id = %s
        ORDER BY id DESC
        LIMIT 1
        """
        cursor.execute(query_photos, (category['id'],))
        photo = cursor.fetchone()
        category['path'] = photo['file_path'] if photo else ''

    cursor.close()
    print(categories)
    return jsonify(categories)

# 传照片的函数
@app.route('/upload/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/upload', filename)

# 照片展示页面的后端：根据点击的相册id展示照片
@app.route('/zhaopianzhanshi', methods=['GET'])
def get_photos():
    category_id = request.args.get('categoryID')
    username = request.args.get('username')

    if not category_id or not username:
        return jsonify({"error": "用户登录和类别状态未保存"}), 400

    cursor = mysql.connection.cursor()

    # 先通过用户名获取用户ID
    query_user_id = "SELECT id FROM users WHERE username = %s"
    cursor.execute(query_user_id, (username,))
    user = cursor.fetchone()
    if not user:
        return jsonify({"error": "用户不存在"}), 400
    user_id = user['id']

    # 然后通过用户ID和类别ID获取照片
    query_photos = """
        SELECT p.id, p.title, p.file_path 
        FROM photos p
        JOIN categories c ON p.category_id = c.id
        WHERE p.category_id = %s AND c.user_id = %s
    """
    cursor.execute(query_photos, (category_id, user_id))
    photos = cursor.fetchall()
    cursor.close()
    print(photos)

    return jsonify(photos)

# 保存注释：根据照片id保存注释
@app.route('/save_annotation', methods=['POST'])
def save_annotation():
    data = request.get_json()
    photo_id = data.get('photo_id')
    annotation = data.get('annotation')
    timestamp = data.get('timestamp')

    if not photo_id or not annotation or not timestamp:
        return jsonify({'error': 'Invalid data'}), 400

    # print('timestamp:',timestamp)
    # 将 ISO 8601 格式的时间转换为 MySQL 格式
    try:
        timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        return jsonify({'error': 'Invalid timestamp format'}), 400

    cur = mysql.connection.cursor()

    # 保存注释和时间
    cur.execute("INSERT INTO annotations (photo_id, annotation, time) VALUES (%s, %s, %s)", 
                (photo_id, annotation, timestamp))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Annotation saved successfully'}), 201

# 展示注释：根据照片id展示注释
@app.route('/show_annotations', methods=['GET'])
def get_annotations():
    photo_id = request.args.get('photo_id')

    if not photo_id:
        return jsonify({'error': 'Invalid photo_id'}), 400

    cur = mysql.connection.cursor()
    cur.execute("SELECT id, annotation, time FROM annotations WHERE photo_id = %s", (photo_id,))
    annotations = cur.fetchall()
    cur.execute("SELECT file_path FROM photos WHERE id = %s", (photo_id,))
    cur.close()
    # 将时间格式化为 ISO 8601 格式
    for annotation in annotations:
        annotation['time'] = annotation['time'].isoformat() + 'Z'  # 确保有 'Z' 作为时区指示符
        # print(annotation)
    
    return jsonify(annotations)

# 照片删除：根据照片id删除照片
@app.route('/delete_photo', methods=['POST'])
def delete_photo():
    data = request.get_json()
    photo_id = data.get('photo_id')

    if not photo_id:
        return jsonify({'error': 'Invalid photo_id'}), 400

    cur = mysql.connection.cursor()
    try:
        # 检查照片是否存在，并获取文件路径
        cur.execute("SELECT file_path, category_id FROM photos WHERE id = %s", (photo_id,))
        photo = cur.fetchone()
        if not photo:
            return jsonify({'error': 'Photo not found'}), 404

        file_path = photo['file_path']
        category_id = photo['category_id']

        # 删除文件
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print(f"文件 {file_path} 不存在，无法删除。")

        # 删除照片对应的注释
        cur.execute("DELETE FROM annotations WHERE photo_id = %s", (photo_id,))
        # 删除照片
        cur.execute("DELETE FROM photos WHERE id = %s", (photo_id,))

        # # 检查是否是该类的最后一张照片
        # cur.execute("SELECT COUNT(*) as count FROM photos WHERE category_id = %s", (category_id,))
        # count_result = cur.fetchone()
        # if count_result['count'] == 0:
        #     # 如果是最后一张照片，删除这个类
        #     cur.execute("DELETE FROM categories WHERE id = %s", (category_id,))

        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'Photo deleted successfully'}), 200

    except Exception as e:
        mysql.connection.rollback()
        cur.close()
        # 记录异常信息到日志，例如使用 logging 模块
        # logging.error("Error occurred: ", exc_info=True)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True,port=5003)
