from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from forms import *
import config

app = Flask(__name__)
app.config.from_object(config.Config)

client = MongoClient("mongodb+srv://MindlessDoc:K.,k.Nbntxrb228!@cluster0.ctgti.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db_name = "Lotos"

collections_admins = client[db_name]["PhotoReports"]

@app.route('/admin', methods=["GET", "POST"])
def index():
    return render_template("admin/header.html")

app.run(port=5099, debug=True)