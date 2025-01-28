import json

import products
from cart import dao
from products import Product


class Cart:
    def init(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    # Retrieve cart details from the data access object (DAO)
    cart_details = dao.get_cart(username)
    
    # Return an empty list if no cart details are found
    if not cart_details:
        return []

    # Use a safer alternative to parse the 'contents', assuming JSON format
    items = []
    for cart_detail in cart_details:
        contents = cart_detail.get('contents', '[]')
        try:
            evaluated_contents = json.loads(contents)
            items.extend(evaluated_contents)
        except json.JSONDecodeError:
            # Log or handle invalid JSON if necessary
            continue

    # Fetch product details for each item and return the list
    return [products.get_product(item) for item in items]

    


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)