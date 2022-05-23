import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

class init_dataBaseConnection:
    def __init__(self, host, user, password, port):
        self.host = host
        self.user = user 
        self.password = password
        self.port = port
        self.cursor = None

    def startConnection(self):
        ''' To start a connection to db'''

        try:
            db = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password, 
                port=self.port)

            self.cursor = db.cursor()

        except pymysql.connect.Error as e:
            print("Error occured while trying to connected ", e)

        except ValueError as e:
            print("Valueerror: ", e)

    def listDatabase(self):
        if self.cursor == None: 
            print("you must execute the startConnection function first")

        else:
            try:
                self.cursor.execute("SHOW databases")
                databases = self.cursor.fetchall()
                print(databases)
            
            except pymysql.connect.Error as e:
                print("Something went wrong ", e)

    def chooseDatabase(self, table):
        if table == None:
            print("you must provide a datbase name")
        elif len(table) == 0:
            print("specify database name, it cannot be an empty string")
        else:

            try:
                self.cursor.execute("use %s" % table)
                print("you now have access to %s table" % table)
            except pymysql.connect.Error as e:
                print(e)
    
    def listTables(self):
        try:
            self.cursor.execute("SHOW tables")
            tables = self.cursor.fetchall()
            print(tables)

        except pymysql.connect.Error as e:
            print("Error ", e)

    def createTable(self):
        creationPath = int(input("creation path: "))

        if creationPath == 1:
            excueteString = input("Enter your comand: ")
            
            try:
                self.cursor.execute(excueteString)

            except pymysql.connect.Error as e:
                print("Error ", e)

        else:

            name = input("Enter database name: ")
            excueteString = "create table %s (" % name
            numOfTabeleRows = int(input("enter the number of attributes: "))

            for i in range(numOfTabeleRows):
                varNameType = input("enter name and type -- example: 'name varchar(22)' of number %s attribute: " % i)
                excueteString += varNameType+", "

            excueteString = excueteString[:-2:]
            excueteString += ")"

            try:
                self.cursor.execute(excueteString)

            except pymysql.connect.Error as e:
                print("Error ", e)

    def dropTable(self, table):
        try:
            self.cursor.execute("drop table %s" % table)
            self.cursor.execute("SHOW tables")
        except pymysql.connect.Error as e:
                print("Error ", e)

    def insertIntoTable(self):
        pass

    def closeConnection(self):
        pass


def main():
    host = os.getenv('host')
    password = os.getenv('password')
    username = os.getenv('user')
    port = int(os.getenv('port'))

    factory = init_dataBaseConnection(host, username, password, port)
    factory.startConnection()
    
    print("--------------------")
    factory.chooseDatabase("project")

    print("-------++++++_-------")
    factory.listTables()

    print("------8*****-------")
    factory.dropTable("test999")

    print("---------=----------")
    factory.listTables()


    return 0


main()

