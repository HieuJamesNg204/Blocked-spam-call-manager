from app.pgUtil import DatabaseUtil as dbutil
from datetime import datetime

def compareDates(date1_str, date2_str):
    try:
        date1 = datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.strptime(date2_str, '%Y-%m-%d')

        if date1 > date2:
            return -1
        elif date1 == date2:
            return 0
        else:
            return 1
    except ValueError:
        print("Date format not valid")
        return -404

def listAll():
    db = dbutil()
    numbers = db.getNumbers()

    instances = []
    for row in numbers:
        item = f"{row[0]} - {row[1]}"
        instances.append(item)
    return instances

def listByDate(blockDate):
    db = dbutil()
    numbers = db.getNumbersByBlockDate(blockDate)

    instances = []
    for row in numbers:
        item = f"{row[0]} - {row[1]}"
        instances.append(item)
    return instances

def listByDateRange(startDate, endDate):
    if compareDates(startDate, endDate) == 1:
        db = dbutil()
        numbers = db.getNumbersByDateRange(startDate, endDate)

        instances = []
        for row in numbers:
            item = f"{row[0]} - {row[1]}"
            instances.append(item)
        return instances
    else:
        return None