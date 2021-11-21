import datetime
import os

from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_cors import CORS
from pymongo import MongoClient
from werkzeug.utils import secure_filename
from flask_login import login_required, login_user, current_user, UserMixin, LoginManager
from werkzeug.security import check_password_hash, generate_password_hash

from forms import *

UPLOAD_FOLDER = 'static/photos/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

client = MongoClient(
    "mongodb+srv://MindlessDoc:K.,k.Nbntxrb228!@cluster0.ctgti.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db_name = "Lotos"

collections_admins = client[db_name]["admins"]
collections_reviews = client[db_name]["reviews"]
collections_prices = client[db_name]["prices"]
collections_booking = client[db_name]["booking"]
collections_photos = client[db_name]["photos"]
collections_orders = client[db_name]["orders"]


login = LoginManager(app)
login.login_view = "login"
login.init_app(app)


class User(UserMixin):

    def __init__(self, id, username, password, name, surname, role):
        self.password_hash = generate_password_hash(password)
        self.username = username
        self.name = name
        self.id = id
        self.surname = surname
        self.role = role

    def get_username(self):
        return self.username

    def check_password(self, password):
        print(password)
        print(self.password_hash)
        return check_password_hash(self.password_hash, password)

    def get_role(self):
        return self.role

    def get_id(self):
        return self.username

    @login.user_loader
    def load_user(username):
        loaded_user = collections_admins.find_one({"username": username})
        return User(loaded_user["_id"], loaded_user["username"], loaded_user["password"], loaded_user["name"],
                    loaded_user["surname"], loaded_user["role"])


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = UserForm()
    if form.is_submitted():
        name = form.username.data
        password = form.password.data
        user_db_count = collections_admins.count_documents({"username": name})
        if user_db_count:
            user_db = collections_admins.find_one({"username": name})
            user = User(user_db["_id"], user_db["username"], user_db["password"], user_db["name"],
                        user_db["surname"], user_db["role"])

            if user is not None and user.check_password(password):
                login_user(user)
                return redirect("/admin")
        flash('Invalid username or password')
        return redirect(url_for('login'))
    return render_template('admin/login.html', title='Sign In', form=form)


@app.route("/status", methods=["GET"])
def status():
    return "Caspian Lotus API is working"


@app.route('/admin', methods=["GET", "POST"])
@login_required
def index():
    return render_template("admin/header.html")


@app.route('/admin/reviews', methods=["GET", "POST"])
@login_required
def reviews():
    return render_template("admin/reviews.html", reviews=collections_reviews.find())


@app.route('/admin/edit_review/<id>', methods=["GET", "POST"])
@login_required
def edit_review(id):
    edit_review_form = EditReviewForm()
    review = collections_reviews.find({"_id": ObjectId(id)})[0]
    if request.method == "GET":
        edit_review_form.review.data = review["review"]
        edit_review_form.photo.data = review["photo"]
        edit_review_form.source_name.data = review["source_name"]
        edit_review_form.source_link.data = review["source_link"]
        edit_review_form.date.data = review["date"]

    if "delete" in request.form:
        collections_reviews.remove({"_id": ObjectId(id)})
        return redirect(url_for("reviews"))

    if edit_review_form.validate_on_submit():
        collections_reviews.update_one({"_id": ObjectId(id)}, {"$set": {
            "name": edit_review_form.name.data,
            "review": edit_review_form.review.data,
            "photo": edit_review_form.photo.data,
            "source_name": edit_review_form.source_name.data,
            "source_link": edit_review_form.source_link.data,
            "date": str(edit_review_form.date.data)
        }})

        return redirect(url_for("reviews"))
    return render_template("admin/edit_review.html", edit_review_form=edit_review_form, review=review)


@app.route('/api/getreviews', methods=['GET'])
def get_reviews():
    return dumps(list(collections_reviews.find())[:3])


@app.route('/api/addreview', methods=["POST"])
def add_review():
    collections_reviews.insert_one({
        "name": request.get_json()["name"],
        "review": request.get_json()["description"]
    })
    return "OK"


@app.route('/admin/addreview', methods=["GET", "POST"])
@login_required
def add_admin_review():
    add_admin_review = AddReviewForm()
    if add_admin_review.validate_on_submit():
        collections_reviews.insert_one({
            "name": add_admin_review.name.data,
            "review": add_admin_review.review.data,
            "photo": add_admin_review.photo.data,
            "source_name": add_admin_review.source_name.data,
            "source_link": add_admin_review.source_link.data,
            "date": add_admin_review.date.data
        })
        return redirect(url_for("reviews"))
    return render_template("admin/addreview.html", add_admin_review=add_admin_review)


@app.route('/admin/prices', methods=["GET", "POST"])
@login_required
def prices():
    return render_template("admin/prices.html", prices=collections_prices.find())


@app.route('/admin/edit_price/<id>', methods=["GET", "POST"])
@login_required
def edit_price(id):
    edit_price_form = EditPriceForm()
    price = collections_prices.find({"_id": ObjectId(id)})[0]
    if request.method == "GET":
        edit_price_form.count.data = price["count"]

    if "delete" in request.form:
        collections_prices.remove({"_id": ObjectId(id)})
        return redirect(url_for("prices"))

    if edit_price_form.validate_on_submit():


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
@login_required
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
@login_required
def photos():
    return render_template("admin/photos.html", photos=collections_photos.find())


@app.route('/admin/edit_photo/<id>', methods=["GET", "POST"])
@login_required
def edit_photo(id):
    edit_photo_form = EditPriceForm()
    filename = collections_photos.find({"_id": ObjectId(id)})[0]
    if "delete" in request.form:
        os.remove('static/' + filename["way"])
        collections_photos.remove({"_id": ObjectId(id)})
        return redirect(url_for("photos"))

    return render_template("admin/edit_photos.html", edit_photo_form=edit_photo_form, filename=filename["way"])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/admin/addphoto', methods=["GET", "POST"])
@login_required
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

    if (endPeriod - startPeriod).days > 20:
        return "fail", 403

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

    if (endPeriod - startPeriod).days > 20:
        return "fail", 403

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


@app.route('/admin/orders', methods=["GET", "POST"])
@login_required
def orders():
    return render_template("admin/orders.html", orders=collections_orders.find())


@app.route("/admin/edit_order/<id>", methods=["GET", "POST"])
@login_required
def admin_edit_order(id):
    edit_order_form = EditOrderForm()
    order = collections_orders.find({"_id": ObjectId(id)})[0]
    if request.method == "GET":
        edit_order_form.startPeriod.data = order["startPeriod"]
        edit_order_form.endPeriod.data = order["endPeriod"]
        edit_order_form.standard.data = order["standard"]
        edit_order_form.lux.data = order["lux"]
        edit_order_form.count.data = order["count"]

    if "delete" in request.form:
        startPeriod = order["startPeriod"];
        endPeriod = order["endPeriod"]
        collections_orders.remove({"_id": ObjectId(id)})
        while startPeriod != endPeriod:
            booking_for_day = collections_booking.find_one({"date": str(startPeriod.date())})
            collections_booking.update_one(
                {"$and": [{"_id": booking_for_day["_id"]}, {"orders": {"$in": [str(id)]}}]},
                {
                    "$inc":
                        {
                            "lux": -order["lux"],
                            "standard": -order["standard"]
                        },
                    "$pull":
                        {
                            "orders": str(id)
                        }
                })
            startPeriod += datetime.timedelta(days=1)
        return redirect(url_for("orders"))

    if edit_order_form.validate_on_submit():

        standard = int(order["standard"])
        lux = int(order["lux"])
        count = int(order["count"])
        startPeriod = order["startPeriod"]
        endPeriod = order["endPeriod"]

        collections_orders.remove({"_id": ObjectId(id)})

        while startPeriod != endPeriod:
            booking_for_day = collections_booking.find_one({"date": str(startPeriod.date())})
            collections_booking.update_one({"$and": [{"_id": booking_for_day["_id"]}, {"orders": {"$in": [str(id)]}}]},
                                           {
                                               "$inc":
                                                   {
                                                       "lux": -lux,
                                                       "standard": -standard
                                                   },
                                               "$pull":
                                                   {
                                                       "orders": str(id)
                                                   }
                                           })
            startPeriod += datetime.timedelta(days=1)

        standard = int(edit_order_form.standard.data)
        lux = int(edit_order_form.lux.data)
        count = int(edit_order_form.count.data)

        startPeriod = edit_order_form.startPeriod.data
        endPeriod = edit_order_form.endPeriod.data

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
        return redirect(url_for("orders"))
    return render_template("admin/edit_order.html", edit_order_form=edit_order_form)


app.run(port=5099, debug=True)
