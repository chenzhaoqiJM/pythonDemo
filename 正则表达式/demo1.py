# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 23:30:48 2021

@author: hp
"""

import re

#正则表达式被编译成模式对象，这些对象具有用于各种操作的方法，例如搜索模式匹配或执行字符串替换。
p = re.compile('[a-e]') #[]代表一个字符类，区分大小写

print(p.findall("Aye, said Mr. Gibenson Stark")) #找寻a-e之间的字符


# \d is equivalent to [0-9].
p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# \d+ will match a group on [0-9], group of one or greater size
p = re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))


print('\n')

# \w is equivalent to [a-zA-Z0-9_].
p = re.compile('\w')
print(p.findall("He said * in some_lang."))

# \w+ matches to group of alphanumeric character.
p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he said *** in some_language."))

# \W matches to non alphanumeric characters.
p = re.compile('\W')
print(p.findall("he said *** in some_language."))


print('\n')
# '*' replaces the no. of occurrence of a character.
p = re.compile('ab*')
print(p.findall("ababbaabbb"))


#############################################################################
print("函数split--------------------------")
print('\n')
#函数split-------根据出现的字符或模式拆分字符串，找到该模式后，字符串中的剩余字符将作为结果列表的一部分返回。
## re.split(pattern, string, maxsplit=0, flags=0)

#第一个参数，pattern 表示正则表达式，string 是将在其中搜索模式并发生拆分的给定字符串，
#如果未提供 maxsplit，则认为是零 '0'，如果提供了任何非零值，则最多发生许多分裂。
#如果 maxsplit = 1，则字符串将只拆分一次，从而得到长度为 2 的列表。 
#flags 非常有用，可以帮助缩短代码，它们不是必需的参数，
#例如：flags = re.IGNORECASE，在此拆分中，大小写将被忽略。

from re import split

# '\W+' denotes Non-Alphanumeric Characters or group of characters
# 找到'，'或空白' '后，split()从该点分割字符串
print(split('\W+', 'Words, words , Words'))
print(split('\W+', "Word's words Words"))

# Here ':', ' ' ,',' are not AlphaNumeric thus, the point where splitting occurs
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))

# '\d+' denotes Numeric Characters or group of characters
# Splitting occurs at '12', '2016', '11', '02' only
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))




# Splitting will occurs only once, at '12', returned list will have length 2
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))

# 'Boy' and 'boy' will be treated same when flags = re.IGNORECASE
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags = re.IGNORECASE))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))



########################################################################
print('\n')
print("函数sub---------------------------------------------")
print('\n')

#函数中的'sub'代表SubString，在给定的字符串（第三个参数）中搜索某个正则表达式模式，
#找到子字符串模式后用repl（第二个参数）替换，计数检查并维护次数出现这种情况。 


# Regular Expression pattern 'ub' matches the string at "Subject" and "Uber".
# As the CASE has been ignored, using Flag, 'ub' should match twice with the string
# Upon matching, 'ub' is replaced by '~*' in "Subject", and in "Uber", 'Ub' is replaced.
print(re.sub('ub', '~*' , 'Subject has Uber booked already', flags = re.IGNORECASE))

# Consider the Case Sensitivity, 'Ub' in "Uber", will not be reaplced.
print(re.sub('ub', '~*' , 'Subject has Uber booked already'))

# As count has been given value 1, the maximum times replacement occurs is 1
print(re.sub('ub', '~*' , 'Subject has Uber booked already', count=1, flags = re.IGNORECASE))

# 'r' before the patter denotes RE, \s is for start and end of a String.
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))



#########################################
#显示了有几个字符串被替换
print('\n')
print("函数subn（）-------------------------------------------")


print(re.subn('ub', '~*' , 'Subject has Uber booked already'))
t = re.subn('ub', '~*' , 'Subject has Uber booked already', flags = re.IGNORECASE)
print(t)
print(len(t))

# This will give same output as sub() would have
print(t[0])


########################################################
print('\n')
print('函数escape------------------------')
#返回所有非字母数字反斜杠的字符串，如果您想匹配可能包含正则表达式元字符的任意文字字符串，这很有用。


# escape() returns a string with BackSlash '\', before every Non-Alphanumeric Character
# In 1st case only ' ', is not alphanumeric
# In 2nd case, ' ', caret '^', '-', '[]', '\' are not alphanumeric
print(re.escape("This is Awseome even 1 AM"))
print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))

