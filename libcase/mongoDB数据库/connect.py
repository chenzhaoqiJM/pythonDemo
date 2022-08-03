# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 11:22:55 2021

@author: hp
"""

import pymongo

# Replace the uri string with your MongoDB deployment's connection string.
conn_str = "mongodb+srv://zq:<SZubyh4RYgT-ZXm>@cluster0.l8rzi.mongodb.net/test?retryWrites=true&w=majority"

# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")