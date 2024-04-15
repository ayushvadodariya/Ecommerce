from flask import Blueprint, jsonify, request

from models.user import User
from models.order import Order

cart_blueprint= Blueprint('cart', __name__)

# @cart_blueprint.route('/<user_id>', methods=['GET'])
# def get_cart(user_id):
#     try:
#         # Retrieve user from the database
#         user = User.objects.get(id=user_id)

#         # Retrieve the cart list from the user object
#         cart_item_ids = user.cart

#         # Fetch details of cart items using the ids
#         cart_items = []
#         for item_id in cart_item_ids:
#             try:
#                 cart_item = Order.objects.get(id=item_id)  # Assuming Order model
#                 cart_items.append(cart_item.to_json())  # Assuming Order model has to_json method
#             except :
#                 pass  # Handle the case where the order with the given ID does not exist

#         return jsonify({'cart': cart_items}), 200
#     except :
#         return jsonify({'error': 'User not found'}), 404

@cart_blueprint.route('/<user_id>', methods=['GET'])
def get_cart(user_id):
    # Retrieve user from the database
    user = User.objects(id=user_id).first()

    if user:
        # Retrieve the cart list from the user object
        cart_list = user.cart

        # return cart_list, 200
        return jsonify({'cart_list': cart_list}), 200

    else:
        return jsonify({'error': 'User not found'}), 404

def calculate_total_order_price(order_ids):
    total_price = 0
    # Iterate over each order ID
    for order_id in order_ids:
        # Retrieve the order from the database
        order = Order.objects(id=order_id).first()
        # If the order exists, add its total price to the total
        if order:
            total_price += order.totalPrice
    return total_price

@cart_blueprint.route('/total-price', methods=['POST'])
def calculate_total_order_price_route():
    # Retrieve order IDs from the request body
    data = request.json
    order_ids = data.get('order_ids', [])

    # Calculate the total price of the given orders
    total_price = calculate_total_order_price(order_ids)

    # Convert the total price to a float
    total_price = float(total_price)

    # Return the total price as a JSON response
    return jsonify({'total_price': total_price}), 200
