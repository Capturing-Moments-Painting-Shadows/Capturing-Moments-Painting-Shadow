from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
from db import db

app = Flask(__name__)
# app.app_context().push()
CORS(app)  # 启用 CORS，允许所有来源的请求

# MySQL数据库配置
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '2365975900lbz'
app.config['MYSQL_DB'] = 'photo_management'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:2365975900lbz@localhost:3306/ayangnote?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
mysql = MySQL(app)

# 处理登录请求
@app.route('/login', methods=['POST'])
def login():
    with app.app_context():
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
    with app.app_context():
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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
