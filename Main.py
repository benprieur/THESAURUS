# -*- coding: utf-8 -*-

from Config import *
from Database import *
import mysql

import sys
import pywikibot
from pywikibot import pagegenerators
import datetime

cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE)
cursor = cnx.cursor()
db = Database(cursor)

siteWiktionary = pywikibot.Site(u'fr', u'wiktionary')

# TUTILS
cursor.execute("SELECT * FROM TUTILS")
row = cursor.fetchone()

if cursor.rowcount == 0:
  print("First get")
else:
  print(row["lastUpdate"])
  datetime_object = datetime.strptime(row["lastUpdate"], '%m/%d/%y %H:%M:%S')

#simpleName = u"Thésaurus en français"
#topCategoryName = u"Catégorie:" + simpleName

new_dict = {}

#category = pywikibot.Category(siteWiktionary, topCategoryName)
#print("this category is analysed..." + topCategoryName)

#for item in category.newest_pages():

#  datetime = item.oldest_revision.timestamp
#  print(datetime)
#  title = item.title()
#  print(title)