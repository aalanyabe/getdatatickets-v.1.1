from flask import Flask, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv(".env")

app = Flask(__name__)

uri = os.getenv("MONGO_URI")
port = os.getenv("PORT")

#create a new cliente and conect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["HelpDesk"]

try:
    client.admin.command('ping')
    print("Pinged your dep")
except Exception as e:
    print(e)

@app.route('/get_tickets',methods=['GET'])

def getTickets():
    ejemplo = list(db.tickets.find({},{"_id":0}))
    return jsonify(ejemplo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))


