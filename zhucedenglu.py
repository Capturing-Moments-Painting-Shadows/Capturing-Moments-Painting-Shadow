from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 启用 CORS，允许所有来源的请求

# MySQL数据库配置
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'photo_management'

mysql = MySQL(app)

# 处理登录请求
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': '用户名和密码不能为空'}), 400

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    cur.close()

    if user and user[2] == password:
        return jsonify({'message': '登录成功'}), 200
    else:
        return jsonify({'message': '用户名或密码错误'}), 400
    
# 处理注册请求
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': '用户名和密码不能为空'}), 400

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        return jsonify({'message': '用户名已存在'}), 400

    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': '注册成功'}), 201

# 处理创建类别请求
@app.route('/create_category', methods=['POST'])
def create_category():
    data = request.json
    username = data.get('username')
    name = data.get('name')
    description = data.get('description')

    if not name or not description:
        return jsonify({'message': '类别名称和描述不能为空'}), 400

    cur = mysql.connection.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()

    if not user:
        return jsonify({'message': '用户不存在'}), 400

    user_id = user[0]
    # 检查是否存在相同用户的相同类型名称的类别
    cur.execute("SELECT * FROM categories WHERE user_id = %s AND name = %s", (user_id, name))
    duplicate_category = cur.fetchone()
    if duplicate_category:
        return jsonify({'message': '类别已存在'}), 400

    cur.execute("INSERT INTO categories (name, user_id, description) VALUES (%s, %s, %s)", 
                (name, user_id, description))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': '类别创建成功'}), 201



if __name__ == '__main__':
    app.run(debug=True, port=5000)
