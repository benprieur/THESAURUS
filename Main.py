# -*- coding: utf-8 -*-

from Config import *
from Database import *
import mysql

import sys
import pywikibot
from pywikibot import pagegenerators
from datetime import datetime
from datetime import date
import time

# CREATION
cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE)
cursor = cnx.cursor()
db = Database(cursor)
db.remove_database(DATABASE)
db.create_database(DATABASE)
db.use_database(DATABASE)
db.create_tables(TABLES, cnx)

# TUTILS
cursor.execute("SELECT * FROM TUTILS")
row = cursor.fetchone()
NEW_UPDATE_DATETIME = {}
CURRENT_UPDATE_DATETIME = {}
print(cursor.rowcount)
if cursor.rowcount == 0 or cursor.rowcount == -1:
  NEW_UPDATE_DATETIME = datetime.utcnow()
  CURRENT_UPDATE_DATETIME = datetime(2000, 1, 1, 12, 0)
  now = NEW_UPDATE_DATETIME.strftime('%Y-%m-%d %H:%M:%S')
  print(now)
  cursor.execute("INSERT INTO TUTILS (name, lastUpdate) VALUES (%s, %s)", ("LAST", now))
  cnx.commit()
else:
  CURRENT_UPDATE_DATETIME = row[1]
  print(CURRENT_UPDATE_DATETIME)
  NEW_UPDATE_DATETIME = datetime.utcnow()
  now = NEW_UPDATE_DATETIME.strftime('%Y-%m-%d %H:%M:%S')
  print(now)
  cursor.execute("UPDATE TUTILS SET lastUpdate = %s WHERE name = %s", (now, "LAST"))
  cnx.commit()

# Wiktionary
siteWiktionary = pywikibot.Site(u'fr', u'wiktionary')
simpleName = u"Thésaurus en français"
topCategoryName = u"Catégorie:" + simpleName

new_dict = {}

category = pywikibot.Category(siteWiktionary, topCategoryName)
print("this category is analysed..." + topCategoryName)

for item in category.newest_pages():
  date_creation_thesaurus = item.oldest_revision.timestamp
  title = item.title()
  print(title)

  print("CURRENT_UPDATE_DATETIME :", CURRENT_UPDATE_DATETIME)

  TTHESAURUS_id = -1
  if date_creation_thesaurus > CURRENT_UPDATE_DATETIME:
    dt = str(date_creation_thesaurus)
    dt = dt.replace("T", " ")
    dt = dt.replace("Z", " ")
    print("date_creation_thesaurus  :", dt)
    # In that case we add an item to the dedicated table
    cursor.execute("INSERT INTO TTHESAURUS (name, creationDateTime) VALUES (%s, %s)", (title, dt))
    cnx.commit()
    TTHESAURUS_id = cursor.lastrowid
  else:
    sql = "SELECT * FROM TTHESAURUS WHERE name = %s"
    adr = (title, )
    cursor.execute(sql, adr)
    results = cursor.fetchall()
    TTHESAURUS_id = results[0][0]

  print("TTHESAURUS_id : ", TTHESAURUS_id)
  currentSize = 0

  for revInfo in item.getVersionHistory():
    # Get revision info
    revId = revInfo.revid
    dt = revInfo.timestamp

    if dt > CURRENT_UPDATE_DATETIME:

      # Get user info
      userName = revInfo.user

      if "Bot" in userName or "bot" in userName:
        continue
      print(userName)
      userInfo = {}
      try:
        userInfo = pywikibot.User(siteWiktionary, userName)
      except:
        continue

      props = userInfo.getprops()

      userId = 0
      try:
        userId = props["userid"]
      except:
        print("Probably an IP")

      isIP = False
      if userId == 0:
        isIP = True

      sql = "SELECT * FROM TUSER WHERE userName = %s"
      adr = (userName, )
      cursor.execute(sql, adr)
      results = cursor.fetchall()

      TUSER_id = -1
      if len(results) == 0:
        cursor.execute("INSERT INTO TUSER (userName, userId, isIP) VALUES (%s, %s, %s)", (userName, userId, isIP))
        TUSER_id = cursor.lastrowid
        cnx.commit()
      else:
        print(results[0])
        TUSER_id = results[0][0]
      print("TUSER_id : ", TUSER_id)

      # Get revision info (2)
      size = len(pywikibot.Page(siteWiktionary, title).getOldVersion(oldid=revId))
      diffSize = size - currentSize
      currentSize = size

      print("TTHESAURUS_id avant insert :" ,TTHESAURUS_id)
      print("TUSER_id avant insert :", TUSER_id)
      sdt = str(dt)
      sdt = sdt.replace("T", " ")
      sdt = sdt.replace("Z", " ")
      cursor.execute("INSERT INTO TREVISION (revId, instant, currentSize, diffSize, idThesaurus, idUser) VALUES (%s, %s, %s, %s, %s, %s)", (revId, sdt, currentSize, diffSize, TTHESAURUS_id, TUSER_id))
      cnx.commit()
      cursor.execute("SELECT * FROM TUSER")
      cursor.fetchall()
      nb1 = cursor.rowcount
      print("Users : ", nb1)

      cursor.execute("SELECT * FROM TREVISION")
      cursor.fetchall()
      nb3 = cursor.rowcount
      print("Revisions : ", nb3)

      cursor.execute("SELECT * FROM TTHESAURUS")
      cursor.fetchall()
      nb2 = cursor.rowcount
      print("Thesaurus : ", nb2)
