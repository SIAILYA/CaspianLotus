from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from pymongo import MongoClient
import datetime
import os
from forms import *
from bson.objectid import ObjectId
from bson.json_util import dumps
from flask_cors import CORS
from werkzeug.utils import secure_filename
from bson.json_util import loads

UPLOAD_FOLDER = 'static/photos/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


client = MongoClient("mongodb+srv://MindlessDoc:K.,k.Nbntxrb228!@cluster0.ctgti.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db_name = "Lotos"

collections_admins = client[db_name]["PhotoReports"]
collections_reviews = client[db_name]["reviews"]
collections_prices = client[db_name]["prices"]
collections_booking = client[db_name]["booking"]
collections_photos = client[db_name]["photos"]
collections_orders = client[db_name]["orders"]


@app.route("/status", methods=["GET"])
def status():
    return "Caspian Lotus API is working"

@app.route('/admin', methods=["GET", "POST"])
def index():
    return render_template("admin/header.html")

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

@app.route('/admin/addreview', methods=["GET", "POST"])
def add_admin_review():
    form = AddReviewForm()
    if form.validate_on_submit():
        collections_reviews.insert_one({
            "name": form.name.data,
            "review": form.review.data
        })
        return redirect(url_for("reviews"))
    return render_template("admin/addreview.html", form=form)

@app.route('/admin/prices', methods=["GET", "POST"])
def prices():
    return render_template("admin/prices.html", prices=collections_prices.find())


@app.route('/admin/edit_price/<id>', methods=["GET", "POST"])
def edit_price(id):
    edit_price_form = EditPriceForm()
    price = collections_prices.find({"_id": ObjectId(id)})[0]
    if request.method == "GET":
        edit_price_form.count.data = price["count"]

    if edit_price_form.validate_on_submit():
        if edit_price_form.validate_on_submit():
            if "delete" in request.form:
                collections_prices.remove({"_id": ObjectId(id)})
                return redirect(url_for("prices"))

        collections_prices.update_one({"_id": ObjectId(id)}, {"$set": {
            "name": edit_price_form.name.data,
            "count": int(edit_price_form.count.data)
        }})
        return redirect(url_for("prices"))
    return render_template("admin/edit_price.html", edit_price_form=edit_price_form, price=price)


@app.route('/api/get_prices', methods=['GET'])
def get_prices():
    return dumps(collections_prices.find())

@app.route('/admin/addprice', methods=["GET", "POST"])
def add_admin_price():
    form = EditPriceForm()
    if form.validate_on_submit():
        collections_prices.insert_one({
            "name": form.name.data,
            "count": int(form.count.data)
        })
        return redirect(url_for("prices"))
    return render_template("admin/addprice.html", form=form)


@app.route('/admin/photos', methods=["GET", "POST"])
def photos():
    return render_template("admin/photos.html", photos=collections_photos.find())


@app.route('/admin/edit_photo/<id>', methods=["GET", "POST"])
def edit_photo(id):
    edit_photo_form = EditPriceForm()
    filename = collections_photos.find({"_id": ObjectId(id)})[0]
    if "delete" in request.form:
        os.remove('static/' + filename["way"])
        collections_photos.remove({"_id": ObjectId(id)})
        return redirect(url_for("photos"))

    return render_template("admin/edit_photos.html", edit_photo_form=edit_photo_form, filename=filename["way"])


def add_admin_photo():
    add_photo_form = AddPhotoForm()
    if add_photo_form.validate_on_submit():
        photo = add_photo_form.photo
        if photo and allowed_file(photo.data.filename):
            filename = secure_filename(photo.data.filename)
            photo.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            collections_photos.insert_one({
                'way': 'photos/' + filename
            })
            return redirect(url_for("photos"))
    return render_template("admin/addphoto.html", add_photo_form=add_photo_form)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/admin/addphoto', methods=["GET", "POST"])
def add_admin_photo():
    add_photo_form = AddPhotoForm()
    if add_photo_form.validate_on_submit():
        photo = add_photo_form.photo
        if photo and allowed_file(photo.data.filename):
            filename = secure_filename(photo.data.filename)
            photo.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            collections_photos.insert_one({
                'way': 'photos/' + filename
            })
            return redirect(url_for("photos"))
    return render_template("admin/addphoto.html", add_photo_form=add_photo_form)


@app.post("/api/check_booking")
def booking_check():
    booking_info = request.get_json()
    count = int(booking_info["count"])
    startPeriod = datetime.datetime.strptime(booking_info["dateStart"], "%Y-%m-%d")
    endPeriod = datetime.datetime.strptime(booking_info["dateEnd"], "%Y-%m-%d")

    lux = 4
    standard = 40

    max_lux_not_allowed = 0
    max_standard_not_allowed = 0

    while startPeriod != endPeriod:
        booking_for_day = collections_booking.find_one({"date": str(startPeriod.date())})

        if booking_for_day is None:
            pass
        else:
            if booking_for_day["lux"] > max_lux_not_allowed:
                max_lux_not_allowed = booking_for_day["lux"]
            if booking_for_day["standard"] > max_standard_not_allowed:
                max_standard_not_allowed = booking_for_day["standard"]

        startPeriod += datetime.timedelta(days=1)

    return {"standard": standard - max_standard_not_allowed, "lux": lux - max_lux_not_allowed}


@app.post("/api/confirm_booking")
def confirm_booking():
    booking_info = request.get_json()
    standard = int(booking_info["standard"])
    lux = int(booking_info["lux"])
    count = int(booking_info["count"])
    startPeriod = datetime.datetime.strptime(booking_info["dateStart"], "%Y-%m-%d")
    startPeriodNE = datetime.datetime.strptime(booking_info["dateStart"], "%Y-%m-%d")
    endPeriod = datetime.datetime.strptime(booking_info["dateEnd"], "%Y-%m-%d")

    order_id = collections_orders.insert_one({"standard": standard,
                                              "lux": lux,
                                              "count": count,
                                              "startPeriod": startPeriod,
                                              "endPeriod": endPeriod}).inserted_id

    while startPeriod != endPeriod:
        booking_for_day = collections_booking.find_one({"date": str(startPeriod.date())})

        if booking_for_day is None:
            collections_booking.insert_one({
                "date": str(startPeriod.date()),
                "lux": int(lux),
                "standard": int(standard),
                "count": count,
                "orders": [str(order_id)]
            })
        else:
            collections_booking.update_one({"_id": booking_for_day["_id"]},
                                           {
                                               "$inc":
                                                   {
                                                       "lux": lux,
                                                       "standard": standard
                                                   },
                                               "$push":
                                                   {
                                                       "orders": str(order_id)
                                                   }
                                           })

        startPeriod += datetime.timedelta(days=1)

    return "Confirmed"


app.run(port=5099, debug=True)
