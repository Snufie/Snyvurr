from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

users = [
    {'username': 'admin', 'password': 'admin', "token": "E3bingus"},
]

@app.route('/login', methods=['POST'])
def login():
    print("recieved request")
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    for user in users:
        if user['username'] == username and user['password'] == password:
            print("user found")
            # Gebruiker is ingelogd, genereer een autorisatietoken en stuur het terug
            return jsonify({"token": {user['token']}}), 200
    return jsonify({"error": "Ongeldige inloggegevens"}), 401

@app.route('/userdata/<token>', methods=['GET'])
def userdata(token):
    print("recieved request")
    data = request.get_json()

if __name__ == '__main__':
    app.run()