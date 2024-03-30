from pymongo import MongoClient
# mongodb+srv://atanu:<password>@ssensor.rqglebz.mongodb.net/?retryWrites=true&w=majority&appName=ssensor
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://atanu:atanu_mongoDB@ssensor.rqglebz.mongodb.net/?retryWrites=true&w=majority&appName=ssensor"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db =client.get_database("ineuron")
