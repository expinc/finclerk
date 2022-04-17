from flask import Blueprint
from flask import render_template

blueprint = Blueprint("journal", __name__)

@blueprint.route("/")
def index():
    return render_template("journal/index.html")
