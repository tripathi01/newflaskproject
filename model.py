import json

def load_json():
    with open('products.json', 'r') as f:
        return json.load(f)

db = load_json()