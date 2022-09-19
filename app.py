from flask import Flask, render_template
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/cats", methods=["GET"])
def cats():
    return render_template("cats.html")

@app.route("/cats/<int:id>", methods=["GET"])
def cat_show(id):
    return render_template("cat.html")
    

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
