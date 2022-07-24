#!/usr/bin/python

import os
from flask import Flask, render_template, request, redirect, url_for, flash
from os import path
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo import MongoClient

if path.exists("env.py"):
    import env


app = Flask(__name__)
debug = True  # os.environ.get("DEBUG")
app.config["MONGO_DBNAME"] = "GoldenShoe"
db = MongoClient('mongodb+srv://admin:JqFLrW17ywlNBoUy@goldenshoe.0oena.mongodb.net/?retryWrites=true&w=majority')
# MONGO_URI = os.environ.get("MONGO_URI")
app.config["MONGO_URI"] = 'mongodb+srv://admin:JqFLrW17ywlNBoUy@goldenshoe.0oena.mongodb.net/?retryWrites=true&w=majority'
# JqFLrW17ywlNBoUy
mongo = PyMongo(app)
app.config.update(SECRET_KEY=os.urandom(24))


@app.route("/")
def home():
    carousel = db.GoldenShoe.products.find()
    products = list(carousel)[-5:]
    return render_template('home.html', products=products)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT'
            )), debug=True)