from flask import Blueprint, render_template,  redirect, url_for, request, jsonify
from models.user import User 


user_blueprint= Blueprint('user', __name__)

  

@user_blueprint.route('/')
def userDetail():
  return {"name": "ayush"}

@user_blueprint.route('/signup', methods=['POST'])
def signup():
    # Retrieve data from the request body
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Check if email and password are provided
    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    # Check if user already exists with the provided email
    existing_user = User.objects(email=email).first()
    if existing_user:
        return jsonify({'error': 'User already exists with this email'}), 400

    # Create a new user
    new_user = User(email=email, password=password)
    new_user.save()

    return jsonify({
          'message': 'Signup successful',
          'userId': str(new_user.id)  # Convert ObjectId to string
          }), 200


@user_blueprint.route('/login', methods=['POST'])
def login():
    # Retrieve data from the request body
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Check if email and password are provided
    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    # Find the user by email
    user = User.objects(email=email).first()

    # Check if user exists and if the password is correct
    if user and user.check_password(password):
        # You may want to generate a token here for authentication
        return jsonify({'message': 'Login successful', 'userId': str(user.id)}), 200
    else:
        return jsonify({'error': 'Invalid email or password'}), 401

