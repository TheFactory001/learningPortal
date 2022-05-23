import pymysql
import os
from dotenv import load_dotenv
load_dotenv()
host = os.getenv('host')
password = os.getenv('password')
username = os.getenv('user')
port = int(os.getenv('port'))



db = pymysql.connect(host, username, password, port)
cursor = db.cursor()
cursor.execute("SHOW databases")
cursor.execute("use project")

cursor.execute("SHOW tables")
r = cursor.fetchall()
print(r)
print("------------------")

cursor.execute("create table test99 (name varchar(20), age varchar(3))")
cursor.execute("SHOW tables")
r = cursor.fetchall()
print("tables tees ", r)

print("---***********-------")
cursor.execute("drop table test99")
cursor.execute("SHOW tables")
x = cursor.fetchall()

print(x)