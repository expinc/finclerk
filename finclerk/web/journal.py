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
    products = journal.get_products_in_account(g.account.id)
    return render_template("journal/index.html", products=products)

@blueprint.route("/products/create", methods=("GET", "POST"))
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
            error = str(ex)

        if error is not None:
            flash(error)
        else:
            return redirect(url_for("journal.index"))

    return render_template("journal/create_product.html")

@blueprint.route("/products/<int:product_id>/trades")
@auth.login_required
def trades(product_id):
    product = journal.get_product(product_id)
    trades = journal.get_trades_of_product(product_id)
    return render_template("journal/trades.html", product=product, trades=trades)

@blueprint.route("/products/<int:product_id>/trades/create", methods=("GET", "POST"))
@auth.login_required
def create_trade(product_id):
    product = journal.get_product(product_id)
    if request.method == "POST":
        side = request.form["side"]
        price = float(request.form["price"])
        quantity = float(request.form["quantity"])
        date = request.form["date"]

        error = None
        try:
            journal.add_trade(product.id, side, price, quantity, date)
        except Exception as ex:
            error = str(ex)

        if error is not None:
            flash(error)
        else:
            return redirect(url_for("journal.trades", product_id=product.id))

    return render_template("journal/create_trade.html", product=product)

@blueprint.route("/products/<int:product_id>/trades/<int:trade_id>/update", methods=("GET", "POST"))
@auth.login_required
def update_trade(product_id, trade_id):
    product = journal.get_product(product_id)
    trade = journal.get_trade(trade_id)
    if request.method == "POST":
        side = request.form["side"]
        price = float(request.form["price"])
        quantity = float(request.form["quantity"])
        date = request.form["date"]

        error = None
        try:
            journal.update_trade(trade.id, side, price, quantity, date)
        except Exception as ex:
            error = str(ex)

        if error is not None:
            flash(error)
        else:
            return redirect(url_for("journal.trades", product_id=product.id))

    return render_template("journal/update_trade.html", product=product, trade=trade)

@blueprint.route("/products/<int:product_id>/trades/<int:trade_id>/delete")
@auth.login_required
def delete_trade(product_id, trade_id):
    journal.delete_trade(trade_id)
    return redirect(url_for("journal.trades", product_id=product_id))
