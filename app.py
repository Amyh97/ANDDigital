#!/usr/bin/python

import os
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo import MongoClient


app = Flask(__name__)
debug = 'DEVELOPMENT' in os.environ
app.config["MONGO_DBNAME"] = "GoldenShoe"
# MONGO_URI = os.environ.get("MONGO_URI")
MONGO_URI = 'mongodb+srv://admin:JqFLrW17ywlNBoUy@goldenshoe.0oena.mongodb.net/?retryWrites=true&w=majority'
app.config["MONGO_URI"] = MONGO_URI
db = MongoClient(MONGO_URI)
mongo = PyMongo(app)
app.config.update(SECRET_KEY=os.urandom(24))


@app.route("/")
def home():
    carousel = db.GoldenShoe.products.find()
    items = list(carousel)[-5:]
    return render_template('home.html', items=items)


@app.route("/products", methods=["GET"])
def view_products(department=None, sale=False):
    query_object = {}
    if request.args.get("department"):
        query_object["department"] = request.args.get("department")
    elif request.args.get("sale"):
        query_object["sale"] = sale
    products = db.GoldenShoe.products.find(query_object)
    return render_template('products.html', products=products)


@app.route("/product_detail/<product_id>/")
def product_detail(product_id):
    product = db.GoldenShoe.products.find_one({"_id": ObjectId(product_id)})
    return render_template("product_detail.html", product=product)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")),
            debug=True)
