from flask import Blueprint, jsonify, request
from models.product import Product
import os
import uuid

product_blueprint= Blueprint('product', __name__)

@product_blueprint.route('/add', methods=['POST'])
def add_product():
    # Retrieve data from the request body
    data = request.json
    name = data.get('name')
    price= data.get('price')
    images= data.get('images')
    description = data.get('description')
    colors = data.get('colors')
    sizes= data.get('sizes')
    brand= data.get('brand')
    for_gender= data.get('for')

    # Create a new product
    new_product = Product(name=name, images=images, price=price, description=description, colors= colors, sizes=sizes, for_gender=for_gender, brand=brand)
    new_product.save()

    return jsonify({'message': 'Product added successfully', 'product_id': str(new_product.id)}), 201

@product_blueprint.route('/<product_id>', methods=['GET'])
def get_product(product_id):
    # Retrieve product details from the database
    product = Product.objects(id=product_id).first()

    if product:
        # Prepare product data to send as response
        product_data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'images': product.images,
            'description': product.description,
            'colors': product.colors,
            'sizes': product.sizes,
            'brand': product.brand,
            'for': product.for_gender
            # Add other product details as needed
        }

        return jsonify(product_data), 200
    else:
        return jsonify({'error': 'Product not found'}), 404

########################################################################______________________####################################____________________##############


@product_blueprint.route('/', methods=['GET'])
def get_all_products():
    try:
        # Retrieve all products from the database
        products = Product.objects.all()

        # Convert products to JSON format
        product_list = [product.to_json() for product in products]

        return jsonify(product_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# @product_blueprint.route("/")
# def allProduct():
#     # data = 
#     data = {
#         "products": [  # Make sure "products" is a string
#             {
#                 "_id": 1,
#                 "name": "SMILEY ® ORIGINALS T-SHIRT",
#                 "price": "1,90.00",
#                 "images": [
#                     "https://static.zara.net/assets/public/8dc5/9efb/f78a42448c49/8329c09e5a59/06050325802-p/06050325802-p.jpg?ts=1709137527423&w=563"
#                 ],
#                 "description": "OVERSIZE - ROUND NECK - NORMAL LENGTH - SHORT SLEEVES",
#                 "colors": ["red", "blue", "black"],
#                 "sizes": ["S", "M", "L", "XL"],
#                 "brand": "ZARA",
#                 "for": "Man"
#             },
#             {
#                 "_id": 2,
#                 "name": "CORDUROY CARGO TROUSERS",
#                 "price": "4,990.00",
#                 "images": [
#                     "https://static.zara.net/assets/public/93d0/b901/27254418a59d/5dcc922f99c7/05520481710-p/05520481710-p.jpg?ts=1704878249184&w=563"
#                 ],
#                 "description": "Relaxed fit trousers. Adjustable elasticated waistband with inner drawstring. Front pockets and rear welt pockets. Flap pockets on the legs. Pleat details on the knees. Adjustable hems with drawstrings. Front zip and button fastening.",
#                 "colors": ["red", "blue", "black"],
#                 "size": ["S", "M", "L", "XL"],
#                 "for": "Man"
#             },
#             {
#                 "_id": 3,
#                 "name": "OVERSIZED HOODIE",
#                 "price": "2,590.00",
#                 "images": [
#                     "https://static.zara.net/assets/public/5c4f/9384/cc024b02a7b8/b5b6191d0bc1/00264052803-p/00264052803-p.jpg?ts=1707994466595&w=563"
#                 ],
#                 "description": "Round neck hoodie with an adjustable drawstring hood. Featuring long sleeves, a contrast slogan and label on the front and matching ribbed trims.",
#                 "colors": ["red", "blue", "black"],
#                 "size": ["S", "M", "L"],
#                 "for": "Woman"
#             },
#             {
#                 "_id": 4,
#                 "name": "STRIPED JACQUARD T-SHIRT X CASA JOSEPHINE",
#                 "price": "2,590.00",
#                 "images": [
#                     "https://static.zara.net/assets/public/5bf2/d4d3/b6934cd298b6/45acc56a1db4/04087436802-p/04087436802-p.jpg?ts=1709048246702&w=563"
#                 ],
#                 "description": "Relaxed fit T-shirt with a round neck and short sleeves. Split hem.@Casa Josephine x Zara special collection",
#                 "colors": ["red", "blue", "black"],
#                 "size": ["S", "M", "L", "XL"],
#                 "for": "Man"
#             },
#             {
#                 "_id": 5,
#                 "name": "VIOLET BLOSSOM 90 ML / 3.04 OZ",
#                 "price": "990.00",
#                 "images": [
#                     "https://static.zara.net/photos///2023/V/2/1/p/0110/410/999/2/w/563/0110410999_6_1_1.jpg?ts=1679046772930"
#                 ],
#                 "description": "A lightning bolt that crosses a cloud of freshness, made up of delicate notes of magnolia, apple and madonna lily.The warmth of vanilla, together with the sweetness of almond, lend comfort and voluptuousness to the fragrance.",
#                 "colors": ["red", "blue", "black"],
#                 "size": ["50ML","90ML", "120ML"],
#                 "for": "both" 
#             },
#             {
#                 "_id": 6,
#                 "name": "TEXTURED TOP",
#                 "price": "1,590.00",
#                 "images": [
#                     "https://static.zara.net/assets/public/bf34/04c9/c7144e9fb6a2/af259aa81b9c/05039342450-p/05039342450-p.jpg?ts=1710343455551&w=563",
#                     "https://static.zara.net/assets/public/a012/072f/4e8642a9b3eb/8c479b1a42c5/05039342450-a1/05039342450-a1.jpg?ts=1710343464229&w=563",
#                     "https://static.zara.net/assets/public/a25c/a26f/e3de41a7ac86/e3a2641ab545/05039342450-a3/05039342450-a3.jpg?ts=1710343456431&w=563",
#                     "https://static.zara.net/assets/public/6304/92bd/e8534d8ba63e/64000e5afd82/05039342450-e3/05039342450-e3.jpg?ts=1710257372713&w=563",
#                     "https://static.zara.net/assets/public/9c19/8d47/0292432ba04a/8b2889ff1970/05039342450-e4/05039342450-e4.jpg?ts=1710257374507&w=563"
#                 ],
#                 "description": "Top with a round neckline and wide straps. Textured fabric.",
#                 "colors": ["red", "blue", "black"],
#                 "size": ["S","M","L"],
#                 "for": "both" 
#             }
#         ]
#     }
#     return jsonify(data) 

# @product_blueprint.route("/<path:productId>")
# def getProduct(productId):
#     print(productId)
#     detail = {
#                 "_id": 6,
#                 "name": "TEXTURED TOP",
#                 "price": "1,590.00",
#                 "image": [
#                     "https://static.zara.net/assets/public/bf34/04c9/c7144e9fb6a2/af259aa81b9c/05039342450-p/05039342450-p.jpg?ts=1710343455551&w=563",
#                     "https://static.zara.net/assets/public/a012/072f/4e8642a9b3eb/8c479b1a42c5/05039342450-a1/05039342450-a1.jpg?ts=1710343464229&w=563",
#                     "https://static.zara.net/assets/public/a25c/a26f/e3de41a7ac86/e3a2641ab545/05039342450-a3/05039342450-a3.jpg?ts=1710343456431&w=563",
#                     "https://static.zara.net/assets/public/6304/92bd/e8534d8ba63e/64000e5afd82/05039342450-e3/05039342450-e3.jpg?ts=1710257372713&w=563",
#                     "https://static.zara.net/assets/public/9c19/8d47/0292432ba04a/8b2889ff1970/05039342450-e4/05039342450-e4.jpg?ts=1710257374507&w=563"
#                 ],
#                 "description": "Top with a round neckline and wide straps. Textured fabric.",
#                 "colors": ["red", "blue", "black"],
#                 "size": ["S","M","L"],
#                 "for": "both" 
#             }

#     return jsonify(detail)

