from . import auth
from .. import analysis
from .. import journal
from flask import Blueprint
from flask import flash
from flask import request
from flask import render_template

blueprint = Blueprint("analysis", __name__)

@blueprint.route("/products/<int:product_id>/earning", methods=("GET", "POST"))
@auth.login_required
def analysis_earning(product_id):
    product = journal.get_product(product_id)
    start_date = None
    end_date = None
    earning = None
    if request.method == "POST":
        start_date = request.form["startDate"]
        end_date = request.form["endDate"]
        error = None
        try:
            earning = analysis.calculate_earning([product_id], start_date, end_date)
        except Exception as ex:
            error = str(ex)

        if error is not None:
            flash(error)

    return render_template("analysis.html", product=product, start_date=start_date, end_date=end_date, earning=earning)
