import os
from flask import Flask
from mongoengine import connect

from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

from blueprints.product import product_blueprint
from blueprints.user import user_blueprint
from blueprints.order import order_blueprint
from blueprints.cart import cart_blueprint



from models.order import Order 
from models.product import Product
from models.user import User




app = Flask(__name__,static_url_path='/uploads')
print(os.getenv('MONGO_CONNECTION_URL'))
connect(host=os.getenv('MONGO_CONNECTION_URL'))


# # product = Product(name = 'Za irt',price = "00")
# # print(product)
# # product.save()
# print("helloooo")
# user = User(name= "ayush")
# print(user.name)
# user.save()

# Enable CORS for all routes
CORS(app)




app.register_blueprint(order_blueprint, url_prefix="/api/v1/order")
app.register_blueprint(product_blueprint ,url_prefix="/api/v1/product")
app.register_blueprint(user_blueprint, url_prefix="/api/v1/user")
app.register_blueprint(cart_blueprint, url_prefix="/api/v1/cart")

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
