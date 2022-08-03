# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import matplotlib.pyplot as plt

import os
import xlwt

dir_path = "E:\\datasets\\zhujian\\leftImg8bit"

if __name__ == '__main__':
    list_file = os.listdir(dir_path) #所有文件读取到列表中，以字符串形式显示
    print(list_file)
    
    for i in range(1, len(list_file)+1):
        try:
            index = list_file[i-1].find('.') #找到后缀名所在之索引
            name_suffix = list_file[i-1][index:] #提取后缀名
            print(name_suffix)
            new_file_name = str(i) + name_suffix #修改为数字加后缀名
            
            ###文件重命名，使用path.join保证路径拼接正确
            os.rename(os.path.join(dir_path, list_file[i-1]), os.path.join(dir_path, new_file_name) )
            
        except :
            print("Please check the format !!!") #发生异常打印信息
            
    print("------END-------")
            