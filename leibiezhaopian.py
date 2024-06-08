from flask import Flask, request, jsonify
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

    print(categories)

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
    category_id = request.form['category_id']
    photo = request.files['file']
    
    if not photo:
        return jsonify({'error': '文件不存在'}), 400

    # 获取类别ID
    cur = mysql.connection.cursor()
    cur.execute("SELECT id,name FROM categories WHERE user_id = %s", (userid,))
    category = cur.fetchone()

    category_name = category['name']
    print(category_name)

    if not category:
        return jsonify({'message': '该类别未创建'}), 400
    
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = 'D:\\Desktop\\cab\\'
    # 确保目录存在
    file_path = os.path.join(current_dir, username, category_name)
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    # 保存文件
    photo.save(file_path)

    cur.execute("INSERT INTO photos (title, category_id, file_path) VALUES (%s, %s, %s)", 
                (title, category_id, file_path))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': '上传成功'}), 200
    # except Exception as e:
    #     return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True,port=5003)
