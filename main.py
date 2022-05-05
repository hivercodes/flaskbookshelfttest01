from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func



#setup app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#create table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

db.create_all()

#CREATE RECORD
#new_book = Book(id=3, title="Starwars", author="Lucas", rating=6.3)
#db.session.add(new_book)
#db.session.commit()

"""
the id field will be auto-generated.



Read All Records
all_books = session.query(Book).all()


Read A Particular Record By Query
book = Book.query.filter_by(title="Harry Potter").first()


Update A Particular Record By Query
book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()


Update A Record By PRIMARY KEY
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()


Delete A Particular Record By PRIMARY KEY
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()
"""



@app.route('/')
def home():
    return render_template("index.html")



@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == "POST":

        new_book = Book(title=request.form["title"], author=request.form["author"], rating=float(request.form["rating"]))
        db.session.add(new_book)
        db.session.commit()
    return render_template("add.html")

all_books = Book.query.filter_by("id")

if __name__ == "__main__":
    app.run(debug=True)
