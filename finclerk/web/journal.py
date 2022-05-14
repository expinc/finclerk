from . import auth
from .. import journal
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

blueprint = Blueprint("journal", __name__)

@blueprint.route("/")
@auth.login_required
def index():
    return render_template("journal/index.html")

@blueprint.route("/createProduct", methods=("GET", "POST"))
@auth.login_required
def create_product():
    if request.method == "POST":
        code = request.form["code"]
        name = request.form["name"]
        type = request.form["type"]
        error = None
        try:
            journal.add_product(g.account.id, code, name, type)
        except Exception as ex:
            print(str(ex))
            error = str(ex)

        if error is not None:
            flash(error)
        else:
            return redirect(url_for("journal.index"))

    return render_template("journal/create_product.html")
