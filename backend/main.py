from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
import os
from forms import *
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson.json_util import loads

import config

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

client = MongoClient("mongodb+srv://MindlessDoc:K.,k.Nbntxrb228!@cluster0.ctgti.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db_name = "Lotos"

collections_admins = client[db_name]["PhotoReports"]
collections_reviews = client[db_name]["reviews"]

@app.route('/admin', methods=["GET", "POST"])
def index():
    return render_template("admin/header.html")

@app.route('/test', methods=["GET", "POST"])
def test():
    form = MessageForm()
    if form.validate_on_submit():
        print(form.name.data)
        print(form.review.data)
        return redirect(url_for("test"))
    return render_template("reviews/addreview.html", form=form)

@app.route('/admin/reviews', methods=["GET", "POST"])
def reviews():
    return render_template("admin/reviews.html", reviews=collections_reviews.find())


@app.route('/admin/edit_review/<id>', methods=["GET", "POST"])
def edit_review(id):
    edit_review_form = EditReviewForm()
    review = collections_reviews.find({"_id": ObjectId(id)})[0]
    if request.method == "GET":
        edit_review_form.review.data = review["review"]

    if edit_review_form.validate_on_submit():
        if "delete" in request.form:
            collections_reviews.remove({"_id": ObjectId(id)})
            return redirect(url_for("reviews"))

        collections_reviews.update_one({"_id": ObjectId(id)}, {"$set": {
            "name": edit_review_form.name.data,
            "review": edit_review_form.review.data
        }})

        return redirect(url_for("reviews"))
    return render_template("admin/edit_review.html", edit_review_form=edit_review_form, review=review)


@app.route('/getreviews', methods=['GET'])
def get_reviews():
    return dumps(collections_reviews.find())


@app.route('/addreview', methods=["POST"])
def add_review():
    collections_reviews.insert_one({
        "name": request.get_json()["name"],
        "review": request.get_json()["description"]
    })
    return "OK"

# @app.route('/addreview', methods=["GET", "POST"])
# def add_review():
#     form = AddReviewForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         review = form.review.data
#         collections_reviews.insert_one({
#             "name": name,
#             "review": review
#         })
#         return redirect(url_for("reviews"))
#     return render_template("reviews/addreview.html", form=form)

app.run(port=5099, debug=True)