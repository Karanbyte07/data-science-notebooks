from flask import request
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        #save the email and password to the database
        return f"<h1>You have successfully logged in {name}</h1>"
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

app.run(debug=True)