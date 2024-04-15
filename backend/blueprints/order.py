from flask import Blueprint, jsonify, request
from models.order import Order 
from models.user import User
import os

order_blueprint= Blueprint('order', __name__)

@order_blueprint.route('/add', methods=['POST'])
def add_product():
    # Retrieve data from the request body
    data = request.json
    orderBy= data.get('orderBy')
    productId= data.get('productId')
    productPrice = data.get('productPrice')
    quantity= data.get('quantity')
    sizes= data.get('sizes')

    # Create a new product
    new_order = Order(
        orderBy=orderBy,
        productId=productId,
        productPrice =productPrice, 
        quantity=quantity,
        sizes=sizes
    )
    new_order.save()

    user = User.objects(id=orderBy).first()

    if user:
        # Add the order ID to the user's cart list
        user.cart.append(str(new_order.id))
        user.save()

    return jsonify({'message': 'Product added successfully', 'order_id': str(new_order.id)}), 201


@order_blueprint.route('/<order_id>', methods=['GET'])
def get_order(order_id):
    # Retrieve order from the database
    order = Order.objects(id=order_id).first()

    if order:
        # Return order details as JSON response
        return jsonify(order.to_json()), 200
    else:
        return jsonify({'error': 'Order not found'}), 404

@order_blueprint.route('/increment_quantity/<order_id>', methods=['GET'])
def increment_quantity(order_id):
    order = Order.objects(id=order_id).first()
    if order:
        new_quantity = order.increment_quantity()
        order.save()
        return jsonify({'new_quantity': new_quantity}), 200
    else:
        return jsonify({'error': 'Order not found'}), 404

@order_blueprint.route('/decrement_quantity/<order_id>', methods=['GET'])
def decrement_quantity(order_id):
    order = Order.objects(id=order_id).first()
    if order:
        new_quantity = order.decrement_quantity()
        order.save()
        return jsonify({'new_quantity': new_quantity}), 200
    else:
        return jsonify({'error': 'Order not found'}), 404
