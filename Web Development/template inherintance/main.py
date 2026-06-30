from flask import Flask, render_template, flash, request

app = Flask(__name__)
app.secret_key = '2580'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    flash("Flash message, this is the first message")
    flash("Flash message, this is the second message")
    flash("Flash message, this is the third message")
    return render_template('about.html')

@app.route('/contact')
def contact():
    name = request.args.get('name')
    language = request.args.get('language')
    return render_template('contact.html', name = name, language = language)
if __name__ == '__main__':
    app.run(debug=True)