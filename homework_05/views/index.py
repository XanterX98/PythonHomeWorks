from flask import (
    Blueprint,
    render_template,
)

main = Blueprint("main", __name__)


@main.get("/", endpoint="index")
def index():
    return render_template("index.html")


@main.get("/about/", endpoint="about")
def about():
    return render_template("about.html")
