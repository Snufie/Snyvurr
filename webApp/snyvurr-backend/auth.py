from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import dotenv
import re

API_key = "boobies"
app = Flask(__name__)
# Sta toegang toe vanuit je Vue.js-domein
CORS(app, origins=["https://snyvurr.vercel.app", "http://localhost:5173"])


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


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'https://snyvurr.vercel.app')
    return response


@app.route('/login', methods=['POST'])
def login():
    print("recieved request")
    print(request.headers.get("X-API_KEY"))
    data = request.get_json()
    api_key = request.headers.get("X-API_KEY")
    if True:
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
    app.run(debug=True)