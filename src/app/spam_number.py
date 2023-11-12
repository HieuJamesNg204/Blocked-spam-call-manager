# This module contains the SpamNumber class that creates an object for each record in the database

from app.pgUtil import DatabaseUtil as dbutil

class SpamNumber:
    def __init__(self, id):
        self.id = id
        self.number = None
        self.blockDate = None
        self.address = None
        self.retrieveNumber()
    
    def retrieveNumber(self):
        db = dbutil()
        row = db.getNumberById(self.id)

        self.number = row[0][1]
        self.blockDate = row[0][2]
        self.address = row[0][3]

    def setNumber(self, number):
        self.number = number
        self.updateDB()
    
    def getNumber(self):
        return self.number
    
    def setBlockDate(self, blockDate):
        self.blockDate = blockDate
        self.updateDB()
    
    def getBlockDate(self):
        return self.blockDate
    
    def setAddress(self, address):
        self.address = address
        self.updateDB()
    
    def getAddress(self):
        return self.address
    
    def updateDB(self):
        db = dbutil()
        db.updateNumber(self.id, self.number, self.blockDate, self.address)