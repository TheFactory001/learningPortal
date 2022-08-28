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

db = pymysql.connect(host=host,user=username,password=pass_word, database=database)
cursor = db.cursor()
#cursor.execute("CREATE TABLE TestSyntax(id varchar(10), image varchar(80), primary key(id))")
#cursor.execute("select * from TestImages")
#print(cursor.fetchall())

def insertImageIntoDatabase():
    sql = "INSERT INTO TestImages (`id`, `image`) VALUES (%s, %s)"
    imageBinaryData = convertToBinaryData("factory.jpg")
    imageId  = ''.join(random.choices(string.digits + string.ascii_letters, k=8))
    ownerId  = ''.join(random.choices(string.digits + string.ascii_letters, k=8))
    
    cursor.execute(sql, (imageId, imageBinaryData))

    db.commit()

def getEncodedImage():
    cursor.execute("select * from TestImages")
    data = cursor.fetchall()
    binaryData = data[0][1] 
    write_file(binaryData, "result/retreivedImage.jpg")
