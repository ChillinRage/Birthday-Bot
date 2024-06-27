import smtplib
from data import (getNameList, getAccountDetails)
from util import (getAge, formatDate, isToday)


class Bot:
    def __init__(self):
        self.header = []
        self.nameList = []
        self.myEmail = ""
        self.botEmail = ""
        self.password = ""
        self.connector = None

        self.__fetchData()

    def __rowToObject(self, row: list) -> dict:
        dataObject = dict()
        for i in range(len(row)):
            dataObject[self.header[i]] = row[i]
        return dataObject

    def __fetchData(self) -> None:
        self.header, nameList = getNameList()
        self.nameList = list(map(lambda row: self.__rowToObject(row), nameList))
        self.myEmail, self.botEmail, self.password = getAccountDetails()

    def getBirthdayList(self) -> list:
        birthdayList = filter(
            lambda row:  isToday(formatDate(row["date"])),
            self.nameList)
        return list(birthdayList)

    def login(self):
        self.connector = smtplib.SMTP('smtp.gmail.com', 587)
        self.connector.starttls()
        self.connector.login(self.botEmail, self.password)

    def logout(self):
        self.connector.close()

    def sendMessage(self, person):
        targetMessage, myMessage = Bot.getMessage(person)
        self.connector.sendmail(self.botEmail, person["email"], targetMessage)
        self.connector.sendmail(self.botEmail, self.myEmail, myMessage)

    @staticmethod
    def getMessage(person: dict) -> (str, str):
        age = getAge(person["date"])
        targetSubject = f"Happy {age} Birthday!"
        mySubject = f"It's {person["name"]}'s Birthday!"

        body = ("Regardless of how bright or dark yesterday has been, rejoice in this special day of the year,\n"
                "go out with friends or family, spend time by yourself. As long as you've fun I suppose."
                "\n\n\n\n"
                "Beep Beep Boop Boop. This is a birthday wish sent from someone who got your info from a national\n"
                "data breach. Do not panic. Do not fret. I am not coming for you."
                "\n\n"
                f"Sike! The name of the person can be found in the email address. Have a great day, {person["name"]}!")

        return f"Subject:{targetSubject}\n\n{body}", f"Subject:{mySubject}\n\n{body}"
