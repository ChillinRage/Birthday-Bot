from datetime import date
from util import formatDate

LOG_PATH = r"./data/logbook.txt"


def createLogbook():
    with open(LOG_PATH, "w") as file:
        file.write("1/1/1900")


def checkToday() -> bool:  # check if logbook's last update date is today
    try:
        with open(LOG_PATH, "r") as file:
            logDate = formatDate(file.read())
            return logDate == date.today()

    except FileNotFoundError:
        createLogbook()
        return False


def update() -> None:  # updates logbook with today's date
    with open(LOG_PATH, "w") as file:
        today = date.today()
        file.write(f"{today.day}/{today.month}/{today.year}")  # saved in format day/month/year
