from flask import Blueprint, request
from models.users import Users

user = Blueprint('user', __name__)

userModel = Users()

@user.route('/register', methods=['POST'])
def register():
    """
    Register a new user.

    Returns:
        dict: A message indicating success or failure of the registration process.
    
    Raises:
        Exception: If an error occurs during user registration.
    """
    try:
        name = request.json.get('name')
        email = request.json.get('email')
        password = request.json.get('password')

        if not name or not email or not password:
            return {'message': 'Please provide all required fields'}, 400

        if userModel.find_one({'email': email}):
            return {'message': 'User with this email already exists'}, 409  # HTTP status code for conflict

        user = userModel.insert({
            'name': name,
            'email': email,
            'password': password
        })

        if not user:
            return {'message': 'Failed to create user'}, 500

        return {'message': 'User created successfully'}, 201  # HTTP status code for created
    except Exception as e:
        print(e)
        return {'message': 'An error occurred while creating the user', 'error': str(e)}, 500
    

@user.route('/login', methods=['POST'])
def login():
    """
    Log in an existing user.

    Returns:
        dict: User information if login successful, otherwise an error message.
    
    Raises:
        Exception: If an error occurs during the login process.
    """
    try:
        email = request.json.get('email')
        password = request.json.get('password')

        if not email or not password:
            return {'message': 'Please provide all required fields'}, 400

        user = userModel.find_one({'email': email})

        if not user or user['password'] != password:
            return {'message': 'Invalid email or password'}, 401

        user['_id'] = str(user['_id'])

        return user
    except Exception as e:
        print(e)
        return {'message': 'An error occurred while logging in', 'error': str(e)}, 500