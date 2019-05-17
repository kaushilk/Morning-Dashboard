import datetime

def todays_date():
    now = datetime.datetime.now()
    weekday = now.strftime("%A")
    month = now.strftime("%B")
    day = now.strftime("%d")
    year = now.strftime("%Y")

    return "{} {} {} {}".format(weekday, month, day, year)
