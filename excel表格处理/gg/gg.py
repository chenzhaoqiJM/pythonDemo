# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 10:16:35 2021

@author: zq
"""

import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import xlwt
import os
import openpyxl

def read_excel(file_path):
    # 打开文件
    path = file_path
    workBook = xlrd.open_workbook(path);

    # 1.获取sheet的名字
    # 1.1 获取所有sheet的名字(list类型)
    # allSheetNames = workBook.sheet_names();
    # print(allSheetNames);

    # 1.2 按索引号获取sheet的名字（string类型）
    # sheet1Name = workBook.sheet_names()[0];
    # print(sheet1Name);

    # 2. 获取sheet内容
    ## 2.1 法1：按索引号获取sheet内容
    sheet1_content1 = workBook.sheet_by_index(0); # sheet索引从0开始

    cols1 = sheet1_content1.col_values(1); # 获取第2列内容,测试时间
    
    cols4 = sheet1_content1.col_values(4)   #获取第5列内容，电压
    
   
    len1 = len(cols1) #打印一下列的长度
    len4 = len(cols4)
    
    print(len1)
    print(len4)
    
    #初始化要写入的文档
    # f = xlwt.Workbook()
    # sheet1 = f.add_sheet('sheet1')
    
    #容量更大
    f = openpyxl.Workbook()
    sheet1 = f.create_sheet(index=0)
    
    pass_flag = False
    w_index = 1
    for i in range(2, len(cols1)):
        
        #头
        if cols1[i] == "静置"  :
            pass_flag = True
            continue
        #尾
        if pass_flag == True and (cols1[i] == "恒流充电" or cols1[i]=="恒流放电"):
            pass_flag = False
        #跳过除开始行的其它中文
        if i!=2 and (cols1[i] == "恒流充电" or cols1[i]=="恒流放电" or cols1[i]=="工步模式" or cols1[i]=="测试时间"):
            continue
            
        if pass_flag == False:
            # sheet1.write(w_index, 0, cols1[i]) #写入第一列
            # sheet1.write(w_index, 1, cols4[i]) #写入第二列
            
            sheet1.cell(column=1, row=w_index, value = cols1[i])
            sheet1.cell(column=2, row=w_index, value = cols4[i])
            w_index+=1 #行索引加1
        else:
            continue

    
    base_path = "C:\\Users\\hp\\Desktop\\gg"    #保存的路径
    path = path.split('\\')[-1] 
    path = path.split('.')[0] + '.xls'
    save_path = os.path.join(base_path, path)   #拼接成完整路径
    f.save(save_path)
    

    return ' ' 

def read_excel2(file_path):
    # 打开文件
    path = file_path
    workBook = xlrd.open_workbook(path);

    # 2. 获取sheet内容
    ## 2.1 法1：按索引号获取sheet内容
    sheet1_content1 = workBook.sheet_by_index(0); # sheet索引从0开始
    
    cols0 = sheet1_content1.col_values(0)
    cols1 = sheet1_content1.col_values(1); # 获取第2列内容,测试时间
    cols2 = sheet1_content1.col_values(2)
    cols3 = sheet1_content1.col_values(3)
    cols4 = sheet1_content1.col_values(4)   #获取第5列内容，电压
    
   
    len1 = len(cols1) #打印一下列的长度
    len4 = len(cols4)
    
    print(len1)
    print(len4)
    #容量更大
    f = openpyxl.Workbook()
    sheet1 = f.create_sheet(index=0)
    
    pass_flag = False
    w_index = 1
    for i in range(2, len(cols1)):
        
        #头
        if cols1[i] == "静置"  :
            pass_flag = True
            continue
        #尾
        if pass_flag == True and (cols1[i] == "恒流充电" or cols1[i]=="恒流放电"):
            pass_flag = False
        #跳过除开始行的其它中文
        if (cols1[i] == "恒流充电" or cols1[i]=="恒流放电" or cols1[i]=="工步模式" or cols1[i]=="测试时间"):
            continue
            
        if pass_flag == False:
            # sheet1.write(w_index, 0, cols1[i]) #写入第一列
            # sheet1.write(w_index, 1, cols4[i]) #写入第二列
            sheet1.cell(column=1, row=w_index, value = cols0[i])
            sheet1.cell(column=2, row=w_index, value = cols1[i])
            sheet1.cell(column=3, row=w_index, value = cols2[i])
            sheet1.cell(column=4, row=w_index, value = cols3[i])
            sheet1.cell(column=5, row=w_index, value = cols4[i])
            w_index+=1 #行索引加1
        else:
            continue

    
    base_path = "C:\\Users\\hp\\Desktop\\gg"    #保存的路径
    path = path.split('\\')[-1] 
    path = path.split('.')[0] + '.xls'
    save_path = os.path.join(base_path, path)   #拼接成完整路径
    f.save(save_path)
    

    return ' ' 

path1 = 'C:\\Users\\hp\\Desktop\\NCSP2.xlsx'
path2 = 'C:\\Users\\hp\\Desktop\\NCSP3.xlsx'
read_excel2(path1)
read_excel2(path2)