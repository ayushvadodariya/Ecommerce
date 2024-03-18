from pkgutil import read_code
from bson import ObjectId
from pymongo import MongoClient
from config import config
import datetime


class Database:
    def __init__ (self):
        self.client=MongoClient(config['db']['url'])
        self.db=self.client[config['db']['name']]

    def insert(self,collection,document):
        document['created_at']=datetime.now()
        document['updated_at']=datetime.now()

        try:
            self.db[collection].insert_one(document)
            return True
        
        except Exception as e:
            print(e)

    def find(self,collection,query)        :
        try:
            return self.db[collection].find(query)
        except Exception as e:
            print(e)
    
    def update_document(self, collection, id, document):
        
        criteria = {"_id":ObjectId(id)}

        document['updated_at']=datetime.now()
        set_obj = {"$set":document}
        try:
            self.db[collection].update_one(criteria, set_obj)
            return True
        except Exception as e:
            print(e)
        
    def delete(self, collection, id):
        try:
            self.db[collection].delete_one({"_id":ObjectId(id)})    
            return True
        except Exception as e:
            print(e)
            