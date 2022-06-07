from flask import Blueprint
import DAO.db_dao as DAO

bp = Blueprint("views", __name__)
streets_db = DAO.StreetsDAO().get_all()
districts_db = DAO.DistrictsDAO().get_all()
volunteers_db = DAO.VolunteersDAO().get_all()


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
