from flask import Blueprint, jsonify, request, render_template
from streets.DAO.db_dao import StreetsDAO, DistrictsDAO, VolunteersDAO
from pprint import pprint as pp

bp = Blueprint("views", __name__, template_folder="templates")
streets_db = StreetsDAO().get_all()
districts_db = DistrictsDAO().get_all()
volunteers_db = VolunteersDAO().get_all()


@bp.route("/streets")
def street_main():
    district_id = request.args.get("district")
    if district_id:
        return jsonify(
            [
                {
                    "id": streets_db[street - 1].id,
                    "title": streets_db[street - 1].title,
                    "volunteer": streets_db[street - 1].volunteer,
                }
                for street in districts_db[int(district_id) - 1].streets
            ]
        )


@bp.route("/districts")
def views_districts():
    return jsonify(
        [{"id": district.id, "title": district.title} for district in districts_db]
    )


@bp.route("/volunteers")
def views_volunteers():
    street_id = request.args.get("streets")
    if street_id:
        return jsonify(
            [
                {
                    "id": volunteers_db[volunteer - 1].id,
                    "name": volunteers_db[volunteer - 1].name,
                    "userpic": volunteers_db[volunteer - 1].userpic,
                    "phone": volunteers_db[volunteer - 1].phone,
                }
                for volunteer in streets_db[int(street_id) - 1].volunteer
            ]
        )


@bp.route("/helpme", methods=["GET", "POST"])
def views_helpme():
    if request.method == "POST":
        return f"I'm a POST method"
    return "I'm a GET method"
