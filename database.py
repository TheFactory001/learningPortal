from unittest import result
import pymysql
import random
import string
import os
from dotenv import load_dotenv
from utilFunctions import *

load_dotenv()

host = os.getenv('host')
pass_word = os.getenv('password')
username = os.getenv('user')
database = os.getenv('database')

db = pymysql.connect(host=host, user=username,
                     password=pass_word, database=database)
cursor = db.cursor()
#cursor.execute("CREATE TABLE TestSyntax(id varchar(10), image varchar(80), primary key(id))")
#cursor.execute("select * from TestImages")
# print(cursor.fetchall())


def insertImageIntoDatabase():
    sql = "INSERT INTO TestImages (`id`, `image`) VALUES (%s, %s)"
    imageBinaryData = convertToBinaryData("factory.jpg")
    imageId = ''.join(random.choices(
        string.digits + string.ascii_letters, k=8))
    ownerId = ''.join(random.choices(
        string.digits + string.ascii_letters, k=8))

    cursor.execute(sql, (imageId, imageBinaryData))

    db.commit()


def getEncodedImage():
    cursor.execute("select * from TestImages")
    data = cursor.fetchall()
    binaryData = data[0][1]
    write_file(binaryData, "result/retreivedImage.jpg")

#:::::::::::::::::::::::CREATE TABLES:::::::::::::::::::::::::::::::::::::
#run create_all_tables() only if not trying to debug

def create_user_table():
    cursor.execute(\
        "CREATE TABLE IF NOT EXISTS USER \
        (user_id INTEGER AUTO_INCREMENT PRIMARY KEY, \
             first_name VARCHAR(50) NOT NULL, \
                last_name VARCHAR(50) NOT NULL, \
                    password VARCHAR(50) NOT NULL, \
                        email VARCHAR(100) UNIQUE NOT NULL, \
                            phone_number VARCHAR(20) UNIQUE) \
                        ")
    db.commit()
    print('user table now exists')
def create_profile_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS profile (profile_id INTEGER AUTO_INCREMENT PRIMARY KEY, \
        user INTEGER UNIQUE NOT NULL, picture BLOB NOT NULL, address VARCHAR(50), city VARCHAR(50), country VARCHAR(50), interests VARCHAR(100), github VARCHAR(50))")
    db.commit()
    print('profile table now exists')


def create_interest_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS INTEREST \
        (id INTEGER AUTO_INCREMENT PRIMARY KEY, \
            user INTEGER NOT NULL, \
                interest VARCHAR(50))")
    db.commit()
    print('interest table now exists')

def create_all_tables():
    create_user_table()
    create_profile_table()
    create_interest_table()
    print('all tables now exist')

#run create_all_tables() here



#:::::::::::::::::::::::::::::::::::::::INSERTING INTO TABLE::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def add_user(first_name,last_name, password, email, phonenumber):
    query = "INSERT INTO person (name, password, email, phonenumber) VALUES (%s, %s, %s, %s)"
    values = (first_name, last_name, password, email, phonenumber)
    cursor.execute(query, values)
    db.commit()


#add_user("daniel", "ob123$", "ob@yahoo.com", 2315639874)

def add_profile(picture, address, city, country, interests, github):
    query = "INSERT INTO profile (picture, address, city, country, interests, github) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (picture, address, city, country, interests, github)
    cursor.execute(query, values)
    db.commit()


#mycursor.execute("SELECT * FROM person")

# for x in mycursor:
 #   print(x)

def get_user_id(email):
    
    cursor.execute(f"SELECT ID FROM USER WHERE EMAIL = \'{email}\'")
    user_id = cursor.fetchall()
    return user_id

def get_person():
    cursor.execute("SELECT * FROM person")
    result = cursor.fetchall()
    # print(result)


# get_person()

def get_email(email):
    query = f"SELECT * FROM person WHERE email = \"{email}\""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)


def get_all_emails():
    cursor.execute('SELECT EMAIL FROM PERSON')

def describe_table(table_name):
    cursor.execute(f'DESCRIBE {table_name}')
    print(cursor.fetchall())

