from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
from forms import *
import config

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(32)

client = MongoClient("mongodb+srv://MindlessDoc:K.,k.Nbntxrb228!@cluster0.ctgti.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db_name = "Lotos"

collections_admins = client[db_name]["PhotoReports"]
collections_reviews = client[db_name]["reviews"]

@app.route('/admin', methods=["GET", "POST"])
def index():
    return render_template("admin/header.html")

@app.route('/reviews', methods=["GET", "POST"])
def reviews():
    return render_template("reviews/reviews.html", reviews=collections_reviews.find())

@app.route('/addreview', methods=["GET", "POST"])
def add_review():
    form = AddReviewForm()
    if form.validate_on_submit():
        name = form.name.data
        review = form.review.data
        collections_reviews.insert_one({
            "name": name,
            "review": review
        })
        return redirect(url_for("reviews"))
    return render_template("reviews/addreview.html", form=form)

app.run(port=5099, debug=True)