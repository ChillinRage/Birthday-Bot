import csv

DATA_PATH = r"./data/data.csv"
ACCOUNT_PATH = r"./data/account.txt"


def getNameList() -> (list, list):
    with open(DATA_PATH, "r", newline='') as file:
        reader = csv.reader(file, delimiter=",")
        header = reader.__next__()
        return header, list(reader)


def getAccountDetails() -> (str, str, str):
    with open(ACCOUNT_PATH, "r", newline='') as file:
        myEmail = file.readline().strip()
        botEmail = file.readline().strip()
        password = file.readline().strip()
        return myEmail, botEmail, password
