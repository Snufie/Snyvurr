from flask import Flask, request, jsonify, make_response, render_template
from flask_mail import Mail, Message
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, decode_token, set_access_cookies, get_jwt, unset_jwt_cookies, unset_access_cookies
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
from datetime import timedelta
import quizDSP as DSP
import config as Config
import os


API_key = "boobies"
API_URL = "https://api-snyvurr.onrender.com"
app = Flask(__name__)


# Allow access from front-end
CORS(app, resources={
    r"/*": {"origins": "https://snyvurr.onrender.com"}
}, allow_headers=["Access-Control-Allow-Origin","Content-Type", "Authorization", "X-API-KEY", "X-FROM-FILE", "X-CSRF-TOKEN"], supports_credentials=True)


jwt = JWTManager(app)
# app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
# app.config["JWT_COOKIE_SECURE"] = True
# app.config["JWT_COOKIE_SAMESITE"] = "None"
# app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
# app.config["JWT_COOKIE_CSRF_PROTECT"] = True
# app.config["JWT_ACCESS_CSRF_HEADER_NAME"] = "X-CSRF-TOKEN"
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=12)
app.config.from_object(Config.config)



auth = HTTPBasicAuth()
tauth = HTTPTokenAuth()
mail = Mail(app)


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

# Check the API key before each HTTP request, except OPTIONS which never has a body
@app.before_request
def apiCheck():
    if request.method != 'OPTIONS':
        providedKey = request.headers.get('X-API-KEY')
        if providedKey == API_key:
            return None
        else:
            return jsonify({'error': 'Invalid API key'}), 401

# Refresh the JWT if it is about to expire
@app.after_request
@auth.login_required
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()['exp']
        now = datetime.now()
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            print("Refreshing token")
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response

    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response

@auth.verify_password
def verify_password(username,password):
    users = DB['users']
    authHeader = request.headers.get('Authorization')
    if authHeader != None:
        try:
            user = users.find_one({"username": username})
            hashedPassword = user["password"]
            if check_password_hash(hashedPassword, password):
                return user
            else:
                return None
        except Exception as error:
            return jsonify({"error": error}), 400
    else:
        return jsonify({"woops!": "No authorization header"}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get('password')
    username = email.split("@")[0]
    users = DB['users']
    try:
        user = users.find_one({"email": email})
        hashedPassword = user["password"]
        if check_password_hash(hashedPassword, password):
            token = create_access_token(identity=email)
            response = make_response(jsonify({'username': username, 'password': password}), 200)
            set_access_cookies(response, token)
            return response
        else:
            return jsonify({"error": "Incorrect password"}), 400
    except Exception as error:
        return jsonify({"error": error}), 400

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get('password')
    username = email.split("@")[0]
    users = DB['users']
    try:
        user = users.find_one({"email": email})
        if user:
            return jsonify({"error": "User already exists"}), 400
        else:
            hashedPassword = generate_password_hash(password)
            users.insert_one({
                "username": username,
                "email": email,
                "password": hashedPassword,
                "verified": False,
                "role": "user",
                "phone": None,
                "verified_phone": False,
                "quizzes": []
                })
            token = create_access_token(identity=email)
            verificationLink = f"http://{API_URL}/verify?token={token}"
            email_body = render_template("register_email.html", verificationLink=verificationLink, user=username)
            msg = Message("Verify your email", sender=os.getenv('MAIL_USERNAME'), recipients=[email])
            msg.html = email_body
            try:
                mail.send(msg)
            except Exception as error:
                return jsonify({"error sending email": error}), 400
            response = make_response(jsonify({"msg": "Successfully registered!"}), 200)
            set_access_cookies(response, token)
            return response
    except Exception as error:
        return jsonify({"error": error}), 400

@app.route('/verify', methods=['GET'])
@jwt_required()
def verifyEmail():
    try:
        urltoken = request.args.get('token')
        token = get_jwt()
        if urltoken == token:
            id = get_jwt_identity()
            users = DB['users']
            user = users.find_one({"email": id})
            user["verified"] = True
            users.update_one({"email": id}, {"$set": user})
            try:
                msg = Message("Email verified", sender=os.getenv('MAIL_USERNAME'), recipients=[user["email"]])
                msg.html = render_template("email_verified.html", user=id)
                mail.send(msg)
            except Exception as error:
                return jsonify({"error sending email": error}), 400
            response = make_response(jsonify({"message": "Successfully verified email"}), 200)
            unset_access_cookies(response)
            return response
        else:
            return jsonify({"error": "Invalid token"}), 400
    except Exception as error:
        return jsonify({"error": error}), 400

@app.route('/getUser', methods=['GET'])
@jwt_required()
def getUser():
    try:
        id = get_jwt_identity()
        print(f"id: {id}")
        users = DB['users']
        user = users.find_one({"email": id})
        username = user.get('username')
        verifiedemail = user.get('verified')
        phone = user.get('phone')
        verifiedphone = user.get('verified_phone')
        role = user.get('role')
        resp = make_response(jsonify({
            "username": username,
            "email": id,
            "verifiedmail": verifiedemail,
            "phone": phone,
            "verifiedphone": verifiedphone,
            "role":role,
            "loggedIn": True}), 200)
        return resp
    except Exception as error:
        response = jsonify({"error": error}), 400
        return response

@app.route("/editUser", methods=['POST'])
@jwt_required()
def editUser():
    try:
        id = get_jwt_identity()
        users = DB['users']
        user = users.find_one({"email": id})
        data = request.get_json()
        email = data.get('email')
        phone = data.get('phone')
        username = data.get('username')
        if email != user["email"]:
            user["email"] = email
            user["verified"] = False
        if phone != user["phone"]:
            user["phone"] = phone
            user["verified_phone"] = False
        if username != user["username"]:
            user["username"] = username
        users.update_one({"email": id}, {"$set": user})
        response = make_response(jsonify({"message": "Successfully edited user"}), 200)
        unset_access_cookies(response)
        set_access_cookies(response, create_access_token(identity=email))
        return response
    except Exception as error:
        return jsonify({"error": error}), 400

@app.route("/getCSRF", methods=['GET'])
@jwt_required()
def getCSRF():
    try:
        csrf = get_jwt()["csrf"]
        print(csrf)
        return jsonify({"csrf": csrf}), 200
    except Exception as error:
        return jsonify({"error": error}), 400

@app.route('/checkAuth', methods=['GET'])
@jwt_required()
def checkAuth():
    try:
        exp_timestamp = get_jwt()['exp']
        now = datetime.now()
        if datetime.timestamp(now) > exp_timestamp:
            return jsonify({"authenticated": False}), 200
        else:
            return jsonify({"authenticated": True}), 200
    except Exception as error:
        return jsonify({"error": error}), 400

@app.route('/logout', methods=['DELETE'])
def logOut():
    try:
        response = make_response(jsonify({"message": "Successfully logged out"}), 200)
        unset_jwt_cookies(response)
        return response
    except Exception as error:
        return jsonify({"error": error}), 400

@app.route('/deleteUser', methods=['DELETE'])
@jwt_required()
def deleteUser():
    try:
        id = get_jwt_identity()
        users = DB['users']
        users.delete_one({"email": id})
        response = make_response(jsonify({"message": "Successfully deleted user"}), 200)
        unset_jwt_cookies(response)
        return response
    except Exception as error:
        return jsonify({"error": error}), 400

@app.route('/study/quiz/create', methods=['POST'])
@jwt_required()
def createQuizDS():
    print(request.cookies.get("csrf_access_token"))
    if request.headers.get("X-FROM-FILE") == 'false':
        try:
            data = request.get_json()
            print(data)
            quizName = data.get("quizName")
            try:
                quizDescription = data.get("quizDescription")
            except:
                quizDescription = ""
            quizData = data.get("quizData")
            print(quizData)
            response = make_response(jsonify({"message": "Successfully"}), 200)
            return response
        except Exception as error:
            return jsonify({"error": error}), 400
    elif request.headers.get("X-FROM-FILE") == "true":
        try:
            data = request.get_data()
            print(data)
            # sep = request.headers.get("X-SEPARATOR")
            # quizType = request.headers.get("X-QUIZTYPE")
            # quizName = request.headers.get("X-QUIZNAME")
            # username = get_jwt_identity()
            users = DB['users']
            nData = request.files['file']
            print(f"nData: {nData}")
            nData.save("test3.txt")
            file = open("test3.txt", "r+")
            nData.close()
            processedData = DSP.processData(file.read(), "dash", "MCQ", "testMCQ", users, "admin", False)
            response = make_response(jsonify({"message": "Successfully created file"}), 200)
            return response
        except Exception as error:
            return make_response(jsonify(f"error: {error}, data: {data}")), 400

@app.route('/study/quiz/get', methods=['GET'])
@jwt_required()
def getQuizDS():
    try:
        users = DB['users']
        id = get_jwt_identity()
        print(id)
        print("ejlfsl ", get_jwt()["csrf"])
        user = users.find_one({"email": id})
        quizzes = user.get("quizzes")
        print(quizzes)
        response = make_response(jsonify({"message": "Successfully", "quizzes": quizzes}), 200)
        return response

    except Exception as error:
        return jsonify({error}), 400




if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5000)