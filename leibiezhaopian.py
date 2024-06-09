from datetime import datetime
from flask import Flask, request, jsonify, send_from_directory
from flask_mysqldb import MySQL
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 启用 CORS，允许所有来源的请求

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'photo_management'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['UPLOAD_FOLDER'] = 'uploads\\'

mysql = MySQL(app)

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
    print("category_id",category_id)
    photo = request.files['file']

    if not photo:
        return jsonify({'error': '文件不存在'}), 400

    # 获取用户ID
    cur = mysql.connection.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    user_id = user['id']
    print("userid",user_id)

    # 获取类别ID
    cur.execute("SELECT name FROM categories WHERE id = %s AND user_id = %s", (category_id, user_id,))
    category = cur.fetchone()

    category_name = category['name']

    if not category:
        return jsonify({'message': '该类别未创建'}), 400
    
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = 'static\\upload\\'
    # 确保目录存在
    file_path = os.path.join(current_dir, username, category_name)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    
    # 获取文件扩展名
    file_extension = os.path.splitext(photo.filename)[1]
    # 拼装新文件名
    new_filename = f"{username}_{category_name}_{title}{file_extension}"    # 有重名风险
    # 保存文件到指定目录
    save_path = os.path.join(file_path, new_filename)

    # 保存文件
    photo.save(save_path)

    cur.execute("INSERT INTO photos (title, category_id, file_path) VALUES (%s, %s, %s)", 
                (title, category_id, save_path))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': '上传成功'}), 200

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
        # 检查照片是否存在
        cur.execute("SELECT category_id FROM photos WHERE id = %s", (photo_id,))
        photo = cur.fetchone()
        if not photo:
            return jsonify({'error': 'Photo not found'}), 404

        category_id = photo['category_id']

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
