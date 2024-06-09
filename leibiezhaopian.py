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

@app.route('/categories', methods=['GET'])
def get_categories():
    username = 'cmy'
    
    # if not username:
    #     return jsonify({'error': '需要提供用户名'}), 400
    
    cur = mysql.connection.cursor()

    # 首先通过用户名查找用户ID
    user_query = "SELECT id FROM users WHERE username = %s"
    cur.execute(user_query, (username,))
    user = cur.fetchone()

    if not user:
        cur.close()
        return jsonify({'error': '用户不存在'}), 400

    print(user)

    # userid = user[0]
    userid = user['id']
    print(userid)

    # 使用用户ID查找分类
    categories_query = """
        SELECT id, name 
        FROM categories 
        WHERE user_id = %s
    """
    cur.execute(categories_query, (userid,))
    categories = cur.fetchall()
    cur.close()

    # print(categories)

    categories_list = [{'id': category['id'], 'name': category['name']} for category in categories]

    return jsonify(categories_list), 200

# 上传照片的 API
@app.route('/upload_photos', methods=['POST'])
def upload_photos():
    # if 'user' not in session:
    #     return jsonify({'message': '用户未登录'}), 400

    # user = session['user']
    userid = 1
    username = 'cmy'

    # try:
    title = request.form['title']
    category_id = request.form['category_name']
    photo = request.files['file']
    
    print(category_id)

    if not photo:
        return jsonify({'error': '文件不存在'}), 400

    # 获取类别ID
    cur = mysql.connection.cursor()
    cur.execute("SELECT name FROM categories WHERE id = %s AND user_id = %s", (category_id, userid,))
    category = cur.fetchone()

    category_name = category['name']
    print(category)

    if not category:
        return jsonify({'message': '该类别未创建'}), 400
    
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = 'upload\\'
    # 确保目录存在
    file_path = os.path.join(current_dir, username, category_name)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    
    # 获取文件扩展名
    file_extension = os.path.splitext(photo.filename)[1]
    # 拼装新文件名
    new_filename = f"{username}_{category_name}_{title}{file_extension}"
    # 保存文件到指定目录
    save_path = os.path.join(file_path, new_filename)
    print(save_path)

    # 保存文件
    photo.save(save_path)

    cur.execute("INSERT INTO photos (title, category_id, file_path) VALUES (%s, %s, %s)", 
                (title, category_id, save_path))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': '上传成功'}), 200
    # except Exception as e:
    #     return jsonify({'error': str(e)}), 500

@app.route('/api/categories', methods=['GET'])
def get_album():
    cursor = mysql.connection.cursor()

    user_id = 1  # Replace with dynamic user ID if needed
    # 第一个查询: 获取用户的所有类别
    query_categories = """
    SELECT id, name
    FROM categories
    WHERE user_id = %s
    """
    cursor.execute(query_categories, (user_id,))
    categories = cursor.fetchall()

    # 第二个查询: 获取每个类别的最新图片路径
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
    # except Error as e:
    #     print(f"Error: {e}")
    #     categories = []
    # finally:
    #     cursor.close()
    #     connection.close()
    # print(categories)
    # print(categories)

    # categories_list = [{'id': category['id'], 'name': category['name'], 'path': categories['path']} for category in categories]
    cursor.close()
    return jsonify(categories)

@app.route('/upload/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/upload', filename)

@app.route('/show_photos', methods=['GET'])
def get_photos():
    categories_id = request.args.get('categoryId')
    user_id = request.args.get('userId')

    if not categories_id or not user_id:
        return jsonify({"error": "用户登录和类别状态未保存"}), 400

    cursor = mysql.connection.cursor()

    query = """
        SELECT p.id, p.title, p.file_path 
        FROM photos p
        JOIN categories c ON p.category_id = c.id
        WHERE p.category_id = %s AND c.user_id = %s
    """
    cursor.execute(query, (categories_id, user_id))
    photos = cursor.fetchall()
    # print(photos)
    cursor.close()

    return jsonify(photos)

@app.route('/save_annotation', methods=['POST'])
def save_annotation():
    data = request.get_json()
    photo_name = data.get('photoName')
    annotation = data.get('annotation')

    if not photo_name or not annotation:
        return jsonify({'error': 'Invalid data'}), 400

    cur = mysql.connection.cursor()

    # 查找照片ID
    cur.execute("SELECT id FROM photos WHERE title = %s", (photo_name,))
    photo = cur.fetchone()
    
    if not photo:
        cur.close()
        return jsonify({'error': 'Photo not found'}), 404

    photo_id = photo['id']

    # 保存注释
    cur.execute("INSERT INTO annotations (photo_id, annotation) VALUES (%s, %s)", (photo_id, annotation))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Annotation saved successfully'}), 201

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True,port=5003)
