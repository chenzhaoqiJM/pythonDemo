# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 13:15:28 2021

@author: hp
"""

# importing module
from pymongo import MongoClient

# creation of MongoClient
client=MongoClient()

# Connect with the portnumber and host
client = MongoClient("mongodb://localhost:27017/")

# Access database
mydatabase = client['name_of_the_database']

# Access collection of the database
mycollection = mydatabase['myTable']

# dictionary to be added in the database
rec={
'title': 'MongoDB and Python',
'description': 'MongoDB is no SQL database',
'tags': ['mongodb', 'database', 'NoSQL'],
'viewers': 104
}

rec1={'title':'ZQ'}

# inserting the data in the database
records = mydatabase.myTable.insert(rec)
records = mydatabase.myTable.insert_one(rec1)

print(records)