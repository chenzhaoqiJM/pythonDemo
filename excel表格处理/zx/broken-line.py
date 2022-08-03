# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt

import xlrd
import xlwt

def read_excel():
    # 打开文件
    workBook = xlrd.open_workbook('1.xlsx');

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


    # 4. 获取整行和整列的值（数组）
    cols = sheet1_content1.col_values(0); # 获取第1列内容
    cols1 = cols[2:]
    
    cols = sheet1_content1.col_values(1) #获取第二列内容
    cols2 = cols[2:]
    print(cols);
    return cols1 ,cols2
    

  


if __name__ == '__main__':
    x, y = read_excel() #x y轴的数据

    plt.figure(figsize=(30,21), dpi=300) #生成画布
    
    # 画拟合线
    
    plt.scatter(x, y, color="green", label="sample data", linewidth=2) #画数据点
    plt.plot(x,y,color="red",label="broken line" ,linewidth=2) #画折线
    plt.xlabel("UG2K/V", fontsize=18) #x轴标签
    plt.ylabel("IA/μA", rotation='horizontal', fontsize=18) #y轴标签
    plt.legend()
    plt.show()