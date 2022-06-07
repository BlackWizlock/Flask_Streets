import requests
from pprint import pprint as pp

class Districts:
    def __init__(self, id, title, streets):
        self.id = id
        self.title = title
        self.streets = streets


class DistrictsDAO:
    def load_data(self):
        return requests.get(
            "https://raw.githubusercontent.com/kushedow/flask-html/master/Rest%20project%201/districts.json"
        ).json()

    def get_all(self):
        districts = []
        for key, value in self.load_data().items():
            districts.append(
                Districts(id=key, title=value["title"], streets=value["streets"])
            )
        return districts


class Streets:
    def __init__(self, id, title, volunteer):
        self.id = id
        self.title = title
        self.volunteer = volunteer


class StreetsDAO:
    def load_data(self):
        return requests.get(
            "https://raw.githubusercontent.com/kushedow/flask-html/master/Rest%20project%201/streets.json"
        ).json()

    def get_all(self):
        streets = []
        for key, value in self.load_data().items():
            streets.append(
                Streets(id=key, title=value["title"], volunteer=value["volunteer"])
            )
        return streets


class Volunteers:
    def __init__(self, id, name, userpic, phone):
        self.id = id
        self.name = name
        self.userpic = userpic
        self.phone = phone


class VolunteersDAO:
    def load_data(self):
        return requests.get(
            "https://raw.githubusercontent.com/kushedow/flask-html/master/Rest%20project%201/volunteers.json"
        ).json()

    def get_all(self):
        volunteers = []
        for key, value in self.load_data().items():
            volunteers.append(
                Volunteers(
                    id=key,
                    name=value["name"],
                    userpic=value["userpic"],
                    phone=value["phone"],
                )
            )
        return volunteers


# pp(DistrictsDAO().get_all()[0].title)  # -> 'Прибрежный'
# pp(VolunteersDAO().get_all()[0].phone)  # -> '+7 (929) 288-75-25'
