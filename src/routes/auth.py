from flask import jsonify, request, abort, Blueprint
from datetime import date, datetime
from werkzeug.security import check_password_hash, generate_password_hash
from src.db import get_db
from flask_jwt_extended import create_access_token

auth_blueprint= Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_blueprint.route("/register", methods=['POST'])
def create_user():
    if request.method=="POST":
        db = get_db()
        cursor = db.cursor()

        user_data = request.get_json()


        username = user_data.get('username', '')
        password = user_data.get('password', '')

        if username == '' or password == '':
            return jsonify({"error": "Username and password are required"}), 400

        
        if len(username)<5:
            return jsonify({"error": "Username is too short"}), 400
        
        if len(password)<5:
            return jsonify({"error": "Password is too short"}), 400

        cursor.execute('SELECT * FROM user WHERE username = ?', (username,))

        row = cursor.fetchone()

        if row is not None:
            return jsonify({"error": "Username already taken"}), 400

        hashed_password= generate_password_hash(password)

        cursor.execute(
            'INSERT INTO user (username, password) VALUES (?, ?)',
            (username, hashed_password)
        )

        db.commit()

        return jsonify({"message": "User created successfully"}), 201

@auth_blueprint.route("/login", methods=['POST'])
def get_all_tasks():
    if request.method=="POST":
        db = get_db()
        cursor = db.cursor()

        user_data = request.get_json()

        username = user_data.get('username', '')
        password = user_data.get('password', '')

        if username == '' or password == '':
            return jsonify({"error": "Username and password are required"}), 400

        cursor.execute('SELECT * FROM user WHERE username = ?', (username,))

        row = cursor.fetchone()

        if row is None:
            return jsonify({"error": "Username does not exist"}), 400
        
        if check_password_hash(row[2], password):
            access_token= create_access_token(identity=row[0])

            return jsonify({"data": {
                'username': row[1],
                'access_token': access_token,
            }}), 201
        else:
            return jsonify({"error": "Wrong password"}), 401
