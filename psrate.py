# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:37:06 2021

@author: 36182
"""
import xlrd#导入Excel库
import numpy as np


T_sheet = xlrd.open_workbook("T_data数据汇总.xls")#设置表格路径
xl_sheet = T_sheet.sheet_by_index(0)#设置表格中的sheet
T_date = xl_sheet.row_values(1)#总日期
T_income = xl_sheet.row_values(2)#总收入
T_psrate = xl_sheet.row_values(3)#总客座率
T_outcome = xl_sheet.row_values(4)#总支出
T_flight = xl_sheet.row_values(5)#总航班数
T_sick = xl_sheet.row_values(6)#总生病人数

psrate=np.array(T_psrate[1:]) #去除字符串
print(psrate)

import PIL
import os
from PIL import Image        #模块导入
im = Image.open('images\plane.jpg')#打开飞机图像
print(im.size)#获得图像大小 最初是（500，500）

pix = im.load()#导入像素
width = im.size[0] #获取宽度
height = im.size[1] #获取长度

def n_size(x,y):  #创建一个函数，来改变image大小（resize）
    new_im = im.resize((x,y))
    return new_im.show()

for each in psrate:                  #for循环，根据list中客座率来改变大小
    if 50 <= int(each) < 55:
        n_size(100,100)            #调用函数
        
    elif 55 <= int(each) < 60:
        n_size(200,200)
        
    elif 60 <= int(each) < 65:
        n_size(300,300)
        
    elif 65 <= int(each) < 70:
        n_size(400,400)
        
    elif 70 <= int(each) < 75:
        n_size(500,500)
        
    elif 75 <= int(each) < 80:
        n_size(600,600)
        
    else:
        print("error")
