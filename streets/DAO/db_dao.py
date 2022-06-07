import requests
from pprint import pprint as pp


volunteers = requests.get(
    "https://raw.githubusercontent.com/kushedow/flask-html/master/Rest%20project%201/volunteers.json"
).json()

streets = requests.get(
    "https://raw.githubusercontent.com/kushedow/flask-html/master/Rest%20project%201/streets.json"
).json()

# pp(districts)
# pp(volunteers)
# pp(streets)


class Database:
    def __init__(self, path: str) -> None:
        self.path = path
        self._db = self._get_db()

    def _get_db(self):
        return requests.get(self.path).json()

    @property
    def db(self):
        return self._db


class Streets(Database):
    def __init__(self):
        super().__init__()
    
    def __repr__(self):
        return f"{self._db}"


if __name__ == "__main__":
    districts = Streets(
        "https://raw.githubusercontent.com/kushedow/flask-html/master/Rest%20project%201/districts.json"
    )
    pp(districts.db)
