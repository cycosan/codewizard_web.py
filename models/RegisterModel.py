import pymongo
import bcrypt
from pymongo import MongoClient


class RegisterModel:
    def __init__(self):
        self.client=MongoClient()
        self.db=self.client.codewizard
        self.Users=self.db.users
    def insert_user(self,data):
        hashed=bcrypt.hashpw(data.password.encode('utf8'),bcrypt.gensalt())
        id=self.Users.insert({"username":data.username,"name":data.name,"password":hashed,"email":data.email})
        print("id ",id)
        myuser=self.Users.find_one({"username":data.username})
        if bcrypt.checkpw("GUitar121".encode('utf8'), myuser["password"]):
            print("Macheted")