from jinja2 import debug
from flask import request
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def jinja2():
    name = "karan"
    language = "python"
    return render_template("index.html", name=name, lang=language)


app.run(debug=True)