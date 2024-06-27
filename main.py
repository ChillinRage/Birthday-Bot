from bot import Bot
import logbook

try:
    birthdayBot = Bot()

    print("Checking logbook...")
    if logbook.checkToday(): quit()

    print("Checking birthday list...")
    birthdayList = birthdayBot.getBirthdayList()
    if not birthdayList: quit()

    print("Connecting to email server...")
    birthdayBot.login()

    print("Here's today's birthday people:")
    for person in birthdayList:
        print(f"    {person["name"]}")
        #birthdayBot.sendMessage(person)

    print("Wishes sent. Closing connector...")
    birthdayBot.logout()
    logbook.update()

    input("All's done. Press anything to close window.")

except Exception as e:
    print("ERROR: ", e)
    input("")
