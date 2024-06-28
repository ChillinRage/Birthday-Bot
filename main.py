import logbook
import time
from bot import Bot
from util import setWorkingDirectory


def run():
    setWorkingDirectory()
    birthdayBot = Bot()

    print("Checking logbook...")
    if logbook.checkToday():
        return

    time.sleep(0.3)
    print("Checking birthday list...")
    birthdayList = birthdayBot.getBirthdayList()
    if not birthdayList:
        logbook.update()
        return

    time.sleep(0.3)
    print("Connecting to email server...")
    birthdayBot.login()

    time.sleep(0.3)
    print("Here's today's birthday people:")
    for person in birthdayList:
        print(f"    {person["name"]}")
        birthdayBot.sendMessage(person)

    time.sleep(0.3)
    print("Wishes sent. Closing connector...")
    birthdayBot.logout()
    logbook.update()

    time.sleep(0.3)
    input("All's done. Press enter to close window.")


try:
    run()
except Exception as e:
    print("ERROR: ", e)
    input("")
