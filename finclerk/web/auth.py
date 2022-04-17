from .. import db
from ..model import Account
from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.security import generate_password_hash

blueprint = Blueprint("auth", __name__, url_prefix="/auth")

@blueprint.route("/login", methods=("GET", "POST"))
def login():
    # TODO: implement
    return render_template("auth/login.html")

@blueprint.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        if error is None:
            try:
                with db.database.atomic():
                    Account.create(name=username, password=generate_password_hash(password))
            except Exception as ex:
                error = str(ex)
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/register.html")
