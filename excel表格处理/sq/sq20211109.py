# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 10:16:35 2021

@author: zq
"""

import xlrd
import xlwt


def read_excel():
    # 打开文件
    path = 'C:\\Users\\hp\\Desktop\\1.xlsx'
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

    cols = sheet1_content1.col_values(0); # 获取第1列内容
    cols1 = cols[2]
    datalen = len(cols)
    
    # cols2 = sheet1_content1.col_values(1); # 获取第2列内容
    # print(cols2[0].split(';'))
    # 4. 获取整行和整列的值（数组）
    # row1 = sheet1_content1.row_values(1)
    
    start = True
    
    if start == True:
    #初始化要写入的文档
        f = xlwt.Workbook()
        sheet1 = f.add_sheet('sheet1')
        
        #开始迭代
        w_index = 0
        for i in range(0, datalen):
            temRow = sheet1_content1.row_values(i) #提取第i行
            temcols2 = temRow[1].split(';')
            for item in temcols2:
                sheet1.write(w_index, 0, temRow[0]) #
                sheet1.write(w_index, 1, item) #
                w_index+=1
            
        f.save('D:\\2.xlsx')
    
    return cols1 


read_excel()
