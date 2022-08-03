import sys
import os
from memory_profiler import profile

@profile
def readByLine():
    f = open("C:\\Users\\hp\\Desktop\\ss.txt")
    line = f.readline()
    while line:
        print(line)
        
        line = f.readline()
        
    f.close()

@profile
def readByAll():
    f = open("C:\\Users\\hp\\Desktop\\2.txt")
    text = f.read()
    print(text) 
    f.close()

if __name__ == '__main__':

    #一行一行读取，可以节省内存
    readByLine()
    
    # readByAll()