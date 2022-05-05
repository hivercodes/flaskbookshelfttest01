from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    if len(all_books) > 0:
        return render_template("index.html", all_books=all_books)
    else:
        return render_template("indexempty.html")


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"],
        }
        all_books.append(new_book)
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

