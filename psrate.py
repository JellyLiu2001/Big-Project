# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:37:06 2021

@author: 36182
"""
import xlrd#导入Excel库
import numpy as np


T_sheet = xlrd.open_workbook("C:/Users/36182/Desktop/Big-Project/T_data数据汇总.xls")#设置表格路径
xl_sheet = T_sheet.sheet_by_index(0)#设置表格中的sheet
T_date = xl_sheet.row_values(1)#总日期
T_income = xl_sheet.row_values(2)#总收入
T_psrate = xl_sheet.row_values(3)#总客座率
T_outcome = xl_sheet.row_values(4)#总支出
T_flight = xl_sheet.row_values(5)#总航班数
T_sick = xl_sheet.row_values(6)#总生病人数
print(T_date,T_income,T_psrate,T_outcome,T_flight,T_sick)#打印所有数据

psrate=np.array(T_psrate[1:]) #去除字符串
print(psrate)

import PIL
import matplotlib.pyplot as plt
import os
from PIL import Image        #模块导入A
im = Image.open('plane.png') #打开飞机图像
print(im.size)#获得图像大小 最初是（500，500）

pix = im.load()#导入像素
width = im.size[0] #获取宽度
height = im.size[1] #获取长度

def n_size(x,y):  #创建一个函数，来改变image大小（resize）
    global new_im   #把改成全局
    new_im = im.resize((x,y))   #重新resize
    return new_im.show()

for each in psrate:                  #for循环，根据list中客座率来改变大小
    if 50 <= int(each) < 55:
        n_size(100,100)            #调用函数
        new_im.save('C:/Users/36182/Desktop/new_plane/{0}.png'.format(each))  #归类，一共6种飞机大小
        
    elif 55 <= int(each) < 60:
        n_size(200,200)
        new_im.save('C:/Users/36182/Desktop/new_plane/{0}.png'.format(each))
        
    elif 60 <= int(each) < 65:
        n_size(300,300)
        new_im.save('C:/Users/36182/Desktop/new_plane/{0}.png'.format(each))
        
    elif 65 <= int(each) < 70:
        n_size(400,400)
        new_im.save('C:/Users/36182/Desktop/new_plane/{0}.png'.format(each))
        
    elif 70 <= int(each) < 75:
        n_size(500,500)
        new_im.save('C:/Users/36182/Desktop/new_plane/{0}.png'.format(each))
        
    elif 75 <= int(each) < 80:
        n_size(600,600)
        new_im.save('C:/Users/36182/Desktop/new_plane/{0}.png'.format(each))
        
    else:
        print("error")
        



import re


def plt_images_wall(img_path):
    imgs_path = []
    imgs_name = os.listdir(img_path)

    for img in imgs_name:
        imgs_path.append(os.path.join(img_path + "/", img))

    if int(len(imgs_path) / 2) != 0:   # 行

        for i in range(len(imgs_path)):
            print(int(str(2) + str(int(len(imgs_path) / 2)) + str(i + 1)))
			# 引入正则是为了解决浮点数的错误问题
            tmp = str(int(len(imgs_path) / 2))
            tmp = re.match("[0-9]", tmp)
            tmp = tmp.string

            plt.subplot(int(str(2) + str(tmp) + str(i + 1)))
            plt.title(each)
            plt.axis("on")   # 打开坐标轴
            plt.imshow(Image.open(imgs_path[i]))
        plt.savefig("plt_wall.jpg")

    plt.show()

if __name__ == "__main__":
    plt_images_wall("new_plane") #这段不知道干嘛的，没看懂

plt_images_wall('new_plane')  #此处调用函数，输入'文件夹名称'  
# new_plane文件夹里为 之前 for循环导入的飞机图




