from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo.errors as MongoErr

import os
import re

API_key = "boobies"
app = Flask(__name__)
jwt = JWTManager(app)
key = os.getenv("JWT_SECRET_KEY")
app.config["JWT_SECRET_KEY"] = key
app.secret_key = key

# Sta toegang toe vanuit je Vue.js-domein
CORS(app, origins=["https://snyvurr.vercel.app", "http://localhost:5173"])
auth = HTTPBasicAuth()
tauth = HTTPTokenAuth(scheme='Bearer')


uri = os.getenv('uri')
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
DB = client['snyvurrDB']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

@app.before_request
def api_check():
    if request.method != "OPTIONS":
        print("Checking API key...")
        provided_key = request.headers.get("X-API_KEY")
        print(f"API key to match with: {API_key}")
        print(f"API key provided: {provided_key}")
        if provided_key != API_key:
            return jsonify({"error": "Invalid API key"}), 401
        elif provided_key == API_key:
            return True
        else:
            return jsonify({"error": "Something went wrong"}), 500


@auth.verify_password
def verify_password(username, password):
    print("recieved request\nVerifying password...")
    users = DB['users']
    caller = users.find_one({"email": username})
    password_hash = caller['password']
    if check_password_hash(password_hash, password):
        print("Password verified")
        user = caller['email']
        return user
    else:
        print("Passwords don't match")
        return False

@tauth.verify_token
def verify_token(token):
    print("recieved request\nVerifying token...")
    print(token)
    session_token = session.get("auth_token")
    print(session_token)
    if token == session_token:
        return jsonify({"message": "Token verified"}), 200
    else:
        return False


@app.route('/login', methods=['POST'])
@auth.login_required
def login():
    print("recieved request")
    data = request.get_json()
    email = data.get('email')
    token = create_access_token(identity=email)
    session['auth_token'] = token
    session['user'] = email
    return jsonify({"token": token}), 200


@app.route('/register', methods=['POST'])
def register():
    print("recieved request")
    users = DB['users']
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    # TODO: add email validation
    # TODO: API calls stats, maybe even in graph form
    # TODO: add uuid to user. For snyvurrChat
    try:
        users.insert_one({"email": email, "password": generate_password_hash(password)})
    except Exception as e:
        return jsonify({"error": e}), 500
    return jsonify({"message": "User created"}), 200


@app.route('/getUser', methods=['GET'])
@tauth.login_required
def userdata():
    print("recieved request")
    user = session.get("user")
    users = DB['users']
    try:
        response = users.find_one({"email": user})
        uname = response["email".split('@')[0]].capitalize()
        email = response["email"]
        #... add more data to return
        res = jsonify({"username": uname, "email": email}), 200
    except:
        res = jsonify({"error": f"User with email/identifier '{user}' doesn't exist."}), 401
    return res

if __name__ == '__main__':
    app.run(debug=True)