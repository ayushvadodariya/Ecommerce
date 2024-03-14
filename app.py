from flask import Flask
from pymongo import MongoClient


config = {
    'mongoURI': 'mongodb://localhost:27017',
    'database': 'ecommerce',
    'users': 'users',
    'products': 'products',
    'cart': 'cart'
}

client = MongoClient(config['mongoURI'])
db = client[config['database']]

app = Flask(__name__)


def insert_user(user):
    try:
        db.users.insert_one(user)
        return True
    except Exception as e:
        print("Error while inserting" + e)
        return False


def insert_products(products):
    try:
        db.users.insert_one(products)
        return True
    except Exception as e:
        print("Error while inserting products " + e)
        return False


def add_to_cart(cart):
    try:
        db.users.insert_one(cart)
        return True
    except Exception as e:
        print("Error while inserting cart" + e)
        return False


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
