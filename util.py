from datetime import date


def addPostfix(n: int) -> str:  # add postfix to a number
    ones = n % 10
    if 1 <= ones <= 3:
        return str(n) + [None, 'st', 'nd', 'rd'][ones]
    return str(n) + 'th'


def getAge(birthdate: str) -> str:  # input format: day/month/year
    birthYear = formatDate(birthdate).year
    return addPostfix(date.today().year - birthYear)


def formatDate(stringDate: str) -> date:  # input format: day/month/year
    dateList = stringDate.split("/")[::-1]
    return date(*map(int, dateList))


def isToday(inputDate: date) -> bool:  # checks if input date is today (ignores its year)
    return ((inputDate.day == date.today().day) and
            (inputDate.month == date.today().month))
