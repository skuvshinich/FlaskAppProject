from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/video')
def video():
    return render_template('video.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<string:username>/<int:id>')
def user(username, id):
    return f"Ur info: {username} - {id}"


if __name__ == '__main__':
    app.run(debug=True)
