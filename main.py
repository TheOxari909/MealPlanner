from flask import Flask, render_template, url_for, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recipes")
def recipes():
    return render_template("recipes.html")

app.run(debug=True)