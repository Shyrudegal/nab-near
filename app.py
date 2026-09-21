from flask import Flask, render_template

app = Flask(__name__)
products = [
    {"id": 1, "name": "Oversized Street Tee", "price": 15000, "category": "Men", "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400", "size": "M, L, XL"},
    {"id": 2, "name": "Cargo Pants - Khaki", "price": 22000, "category": "Men", "image": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=400", "size": "S, M, L"},
    {"id": 3, "name": "Satin Mini Dress", "price": 18500, "category": "Women", "image": "https://images.unsplash.com/photo-1595777457583-95e059d581b?w=400", "size": "S, M"},
    {"id": 4, "name": "Vintage Denim Jacket", "price": 25000, "category": "Women", "image": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400", "size": "M, L"},
    {"id": 5, "name": "Crossbody Bag - Black", "price": 12000, "category": "Accessories", "image": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=400", "size": "One Size"},
    {"id": 6, "name": "Chunky Silver Chain", "price": 18000, "category": "Accessories", "image": "https://images.unsplash.com/photo-1611591437281-460bfbe1220a?w=400", "size": "One Size"},
    {"id": 7, "name": "Essential Tee - Black", "price": 12000, "cat": "Clothes", "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab"},
    {"id": 8, "name": "Baggy Cargo Pants", "price": 25000, "cat": "Clothes", "image": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246"},
    {"id": 9, "name": "Oversized Hoodie", "price": 22000, "cat": "Clothes", "image": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea"},
    {"id": 10, "name": "Vintage Shirt", "price": 18000, "cat": "Clothes", "image": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c"},
    {"id": 11, "name": "NAB NEAR Cap", "price": 8500, "cat": "Accessories", "image": "https://images.unsplash.com/photo-1556821840-3a63f95609a7"},
    {"id": 12, "name": "Crossbody Bag", "price": 15000, "cat": "Accessories", "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62"},
    {"id": 13, "name": "Beaded Bracelets Set", "price": 5000, "cat": "Accessories", "image": "https://images.unsplash.com/photo-1611591437281-460bfbe1220a"},
    {"id": 14, "name": "Sunglasses - Black", "price": 7000, "cat": "Accessories", "image": "https://images.unsplash.com/photo-1511499767150-a48a237f0083"},
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000) 