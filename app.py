from flask import Flask, render_template, abort, redirect, url_for, request
from flask_cors import CORS
from werkzeug import exceptions

from db import cats


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else: 
        name = request.form["name"]
        age = request.form["age"]
        breed = request.form["breed"]
        caption = request.form["caption"]
        id = len(cats) + 1
        cats.append({
            "id": id,
            "name": name,
            "age": age,
            "breed": breed,
            "caption": caption
        })
        return redirect(url_for("cat_show", id=id))

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/cats/", methods=["GET"])
def cats_index():
    return render_template("cats.html", cats=cats, title="Our cats")

@app.route("/cats/<int:id>", methods=["GET"])
def cat_show(id):
    matching_cats = [c for c in cats if c['id'] == id]
    if len(matching_cats) == 1:
        cat = matching_cats[0]
        return render_template("cat.html", cat=cat)
    else:
        abort(404)

# Error handlers

@app.errorhandler(exceptions.NotFound)
def page_not_found(error):
    return render_template("errors/404.html"), 404

@app.errorhandler(exceptions.InternalServerError)
def server_error(error):
    return render_template("errors/500.html"), 500

@app.errorhandler(exceptions.BadRequest)
def bad_request(error):
    return render_template("errors/400.html"), 400

if __name__ == "__main__":
    app.run(debug=True)
