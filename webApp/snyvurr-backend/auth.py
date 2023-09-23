from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import dotenv
import re

app = Flask(__name__)
CORS(app)

env = dotenv.find_dotenv("./.env")
uri = dotenv.get_key(env, "uri")
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
DB = client['snyvurrDB']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

api_key = "boobies"


@app.route('/login', methods=['GET'])
def login():
    print("recieved request")
    data = request.get_json()
    api_key = request.headers.get("Z_API_KEY")
    if api_key == "boobies":
        user = data.get('user')
        password = data.get('password')

        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(email_pattern, user):
            identifier = "email"
        else:
            identifier = "username"
        users = DB['users']
        user = users.find_one({identifier: user, "password": password})
        if user != None:
                # Gebruiker is ingelogd, genereer een autorisatietoken en stuur het terug
                return jsonify({"token": {user['token']}}), 200
        else: return jsonify({"error": "Ongeldige inloggegevens"}), 401
    else:
        return jsonify({"error": "Geen geldige API key"}), 401

@app.route('/register', methods=['POST'])
def register(email,password):
    pass

@app.route('/userdata/<token>', methods=['GET'])
def userdata(token):
    print("recieved request")
    data = request.get_json()

if __name__ == '__main__':
    app.run()