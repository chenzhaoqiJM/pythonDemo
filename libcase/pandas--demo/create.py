# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 23:35:54 2021

@author: hp
"""

# import pandas as pd
import pandas as pd

# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks']

# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)


print('\n')
# intialise data of lists.
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}

# Create DataFrame
df = pd.DataFrame(data)

# Print the output.
print(df)


##############################################
print('\n', '通过名字访问列示例')
# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
 
# select two columns
print(df[['Name', 'Qualification']])


###########################################
print('\n', '读取csv文件并访问行--示例')
# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name") #以名字作为索引列
# print(data)
 
# retrieving row by loc method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]
print(first, "\n\n\n", second)

print('\n\n\n')
# retrieving columns by indexing operator
first = data["Age"]
print(first)

print('\n\n\n')
# retrieving rows by iloc method 
row2 = data.iloc[3]
print(row2)

