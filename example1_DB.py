import mysql.connector

class connVacDB:
    def __init__(self):
        self.connDB = mysql.connector.connect(host="localhost", user="root", password="")
        self.cur = self.connDB.cursor()
        self.cur.execute("CREATE DATABASE IF NOT EXISTS vacciendb")
        self.connDB.commit()

        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="vacciendb")
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS listCitizen (
                            icnumber VARCHAR(20) NOT NULL,
                            name VARCHAR(255),
                            age VARCHAR(3),
                            citizen VARCHAR(3),
                            Diabetes VARCHAR(30),
                            Hyper VARCHAR(30),
                            Heart VARCHAR(30),
                            ageStatus VARCHAR(50),
                            vacStatus VARCHAR(50),
                            PRIMARY KEY (icnumber)
                            )""")
        self.conn.commit()
        print("...Successful connection to database...")

# Create an instance of the class to connect to the database and create the table
db = connVacDB()