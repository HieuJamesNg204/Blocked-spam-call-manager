from app.pgUtil import DatabaseUtil as dbutil

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