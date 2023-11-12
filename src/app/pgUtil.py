# This module contains some utilities for database connection and queries

import psycopg2 as pg
from app import config
import sys

class DatabaseUtil:
    def __init__(self, connectionConfig=config.connection_conf):
        self.connectionConfig = connectionConfig
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            # Connect to the database
            self.connection = pg.connect(self.connectionConfig)
            # Define the cursor
            self.cursor = self.connection.cursor()
        except Exception as e:
            # If there is an issue connecting to the database
            print(f"Something went wrong while connecting to the database: {e}")
            sys.exit()
    
    def closeConnection(self):
        self.cursor.close()
        self.connection.close()

    def addNumber(self, number, blockDate, address):
        try:
            self.connect()
            query = f"INSERT INTO spam_list (number, block_date, address) \
                    VALUES (\
                        '{number}', TO_DATE('{blockDate}', 'YYYY-MM-DD'), '{address}' \
                    );"
            self.cursor.execute(query)
            self.connection.commit()
            self.closeConnection()
        except Exception as e:
            print(f"Something has gone wrong while adding the number: {e}")
    
    def getNumbers(self):
        try:
            self.connect()
            query = "SELECT * FROM spam_list ORDER BY id;"
            self.cursor.execute(query)
            res = self.cursor.fetchall()
            self.closeConnection()
            return res
        except Exception as e:
            print(f"Something has gone wrong while retrieving numbers: {e}")
            return []
    
    def getNumberById(self, id):
        try:
            self.connect()
            query = f"SELECT * FROM spam_list WHERE id={id};"
            self.cursor.execute(query)
            res = self.cursor.fetchall()
            self.closeConnection()
            return res
        except Exception as e:
            print(f"Something has gone wrong while retrieving numbers: {e}")
            return []
    
    def updateNumber(self, id, newNumber, newBlockDate, newAddress):
        try:
            self.connect()
            query = f"UPDATE spam_list \
                      SET number='{newNumber}', block_date=TO_DATE('{newBlockDate}', 'YYYY-MM-DD'), address='{newAddress}' \
                      WHERE id={id};"
            self.cursor.execute(query)
            self.connection.commit()
            self.closeConnection()
        except Exception as e:
            print(f"Something has gone wrong while updating the number: {e}")