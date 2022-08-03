# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 13:30:01 2021

@author: hp
"""

from pymongo import MongoClient

try:
	conn = MongoClient()
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")

# database name: mydatabase
db = conn.name_of_the_database

# Created or Switched to collection names: myTable
collection = db.myTable

# print(collection)

# To find() all the entries inside collection name 'myTable'
cursor = collection.find()
for record in cursor:
 	print(record)
    # pass

cursor = collection.find({'title':'ZQ'})
for record in cursor:
    print(record)