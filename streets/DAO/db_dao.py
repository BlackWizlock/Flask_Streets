import requests
from pprint import pprint as pp
from dataclasses import dataclass, field

@dataclass
class Districts:
    id: int
    title: str
    streets: list[int] = field(default_factory=list)


@dataclass
class Streets:
    id: int
    title: str
    volunteer: list[int] = field(default_factory=list)


@dataclass
class Volunteers:
    id: int
    name: str
    userpic: str
    phone: str


class DistrictsDAO:
    def load_data(self):
        return requests.get(
            "https://raw.githubusercontent.com/kushedow/flask-html/master/Rest%20project%201/districts.json"
        ).json()

    def get_all(self):
        districts = []
        for key, value in self.load_data().items():
            districts.append(
                Districts(id=int(key), title=value["title"], streets=value["streets"])
            )
        return districts


class StreetsDAO:
    def load_data(self):
        return requests.get(
            "https://raw.githubusercontent.com/kushedow/flask-html/master/Rest%20project%201/streets.json"
        ).json()

    def get_all(self):
        streets = []
        for key, value in self.load_data().items():
            streets.append(
                Streets(id=int(key), title=value["title"], volunteer=value["volunteer"])
            )
        return streets

    def get_streets(self):
        output = []
        for item in self.get_all():
            output.append(item.id, item.title)
        return output


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
