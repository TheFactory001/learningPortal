from unittest import result
import pymysql
import random
import string
import os
from dotenv import load_dotenv
from utilFunctions import *

load_dotenv()

host = os.getenv('factorydatabase.cx7bcz8zyphb.ca-central-1.rds.amazonaws.com')
pass_word = os.getenv('th3f4ctory')
<<<<<<< Updated upstream
username = os.getenv('admin')
=======
username = os.getenv('user')
>>>>>>> Stashed changes
database = os.getenv('project')

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


<<<<<<< Updated upstream
=======
cursor.execute("CREATE TABLE profile (picture BLOB UNIQUE NOT NULL, address VARCHAR(50), city VARCHAR(50), country VARCHAR(50), interests VARCHAR(100), github VARCHAR(50))")


>>>>>>> Stashed changes
def add_person(name, password, email, phonenumber):
    query = "INSERT INTO person (name, password, email, phonenumber) VALUES (%s, %s, %s, %s)"
    values = (name, password, email, phonenumber)
    cursor.execute(query, values)
    db.commit()


<<<<<<< Updated upstream
=======
#add_person("daniel", "ob123$", "ob@yahoo.com", 2315639874)

>>>>>>> Stashed changes
def add_profile(picture, address, city, country, interests, github):
    query = "INSERT INTO profile (picture, address, city, country, interests, github) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (picture, address, city, country, interests, github)
    cursor.execute(query, values)
    db.commit()


<<<<<<< Updated upstream
def get_person():
    cursor.execute("SELECT * FROM person")
    result = cursor.fetchall()
    print(result)


def get_email(email):
    query = f"SELECT * FROM person \"{email}\""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)


get_email("ob@yahoo.com")


def get_password(password):
    query = f"SELECT * FROM person \"{password}\""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)


def get_name(name):
    query = f"SELECT * FROM person \"{name}\""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)


def get_phonenumber(phonenumber):
    query = f"SELECT * FROM person \"{phonenumber}\""
    cursor.execute(query)
    result = cursor.fetchall()
    print()


def get_city(city):
    query = f"SELECT * FROM profile \"{city}\""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)


def get_country(country):
    query = f"SELECT * FROM profile \"{country}\""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)


def get_interests(interests):
    query = f"SELECT * FROM profile \"{interests}\""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)


def get_github(github):
    query = f"SELECT * FROM profile \"{github}\""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)


def get_country(country):
    query = f"SELECT * FROM profile \"{country}\""
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)


def get_address(address):
    query = f"SELECT * FROM profile \"{address}\""
=======
#mycursor.execute("SELECT * FROM person")

# for x in mycursor:
 #   print(x)


# def get_person():
    cursor.execute("SELECT * FROM person")
    result = cursor.fetchall()
    # print(result)


# get_person()

def get_email(email):
    query = f"SELECT * FROM person \"{email}\""
>>>>>>> Stashed changes
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
