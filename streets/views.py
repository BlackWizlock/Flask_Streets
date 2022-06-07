from flask import Blueprint

bp = Blueprint("views", __name__)


@bp.route("/streets")
def street_main():
    return "I'm a streets"


@bp.route("/districts")
def views_districts():
    return "I'm a district"


@bp.route("/volunteers")
def views_volunteers():
    return "I'm a volunteers"


@bp.route("/helpme")
def views_helpme():
    return "I'm a helpme"
