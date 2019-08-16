from Config import *
from Database import *
import mysql

cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST)
cursor = cnx.cursor()

db = Database(cursor)
db.create_database(DATABASE)
db.use_database(DATABASE)



