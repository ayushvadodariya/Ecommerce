from mongoengine import Document, StringField, ListField

class User(Document):
    name = StringField(required=False) 
    address = StringField(required=False)
    email = StringField(required=False)
    password = StringField(required=False)
    cart = ListField(StringField(), default=[])

    def to_json(self):
        return {
            "name": self.name,
            "address": self.address,
            "email": self.email,
            "password": self.password,
            "cart": self.cart
        }
    def check_password(self, password):
        # Compare the provided password with the stored password
        return self.password == password