from factory.database import Database
from factory.validator import Validator


class Users:
    def __init__ (self):
        self.db=Database()
        self.validator=Validator()
        
        self.collection="users"

        self.fields= {
            'name': 'String',
            'email': 'String',
            'pasword': 'String',
            'created_at': 'datetime',
            'updatded_at': 'datetime'
        }
        self.create_required_fields = [
            'name', 'email', 'password'
        ]

        self.create_optional_fields = []

        self.update_required_fields = [
            'name', 'email', 'password'
        ]

        self.update_optional_fields = []
    def insert(self,document):
        if self.validator.validate(document,self.fields,self.create_required_fields, self.create_optional_fields):
            res= self.db.insert(self.collection, document)
            return res
        else:
            return False
    def find(self,query)    :
        return  self.db.find(self.collection, query)
    
    def update_document(self, id, document):
        if self.validator.validate(document, self.field, self.update_required_fields, self.update_optional_fields):
            return self.db.update_document(self.collection, id, document)

    def delete(self, id):
        return self.db.delete(self.collection, id)
