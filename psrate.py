# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:37:06 2021

@author: 36182
"""
import xlrd
import numpy as np


T_sheet = xlrd.open_workbook("C:/Users/36182/Desktop/Big-Project/T_data数据汇总.xls")#path
xl_sheet = T_sheet.sheet_by_index(0)
T_date = xl_sheet.row_values(1)#date
T_income = xl_sheet.row_values(2)#income
T_psrate = xl_sheet.row_values(3)#psrate
T_outcome = xl_sheet.row_values(4)#outcome
T_flight = xl_sheet.row_values(5)#number of flights
T_sick = xl_sheet.row_values(6)#number of sickness people
print(T_date,T_income,T_psrate,T_outcome,T_flight,T_sick)#print all the date

psrate=np.array(T_psrate[1:]) #remove the string in excel
print(psrate)
date1=np.array(T_date[1:])
print(date1)

dict1=dict(zip(psrate,date1))#create a dictionary
print(dict1)


import matplotlib.pyplot as plt
import os
from PIL import Image       
im = Image.open('C:/Users/36182/Desktop/Big-Project/plane.png') #open the image of the plane
print(im.size)#get the size of the image, whcihc is （500，500）at the beginning

pix = im.load()#pixel
width = im.size[0] #get the width
height = im.size[1] #get the height

def n_size(x,y):  #create a function to resize the image
    global new_im   #change the variable to globale variable
    new_im = im.resize((x,y))   #resize the image
    return new_im


os.mkdir('C:/Users/36182/Desktop/new_plane')#create a file

for each in dict1.keys():    #use for loop to change the size of the image according to the psrate
    if 50 <= float(each) < 55:
        n_size(100,100)          
        new_im.save('C:/Users/36182/Desktop/new_plane/{0}.png'.format(dict1[each])) #use foramt to name the image with the date   
        #save the image in a file
    elif 55 <= float(each) < 60:
        n_size(200,200)
        new_im.save('C:/Users/36182/Desktop/new_plane/{0}.png'.format(dict1[each]))
        
    elif 60 <= float(each) < 65:
        n_size(300,300)
        new_im.save('C:/Users/36182/Desktop/new_plane/{0}.png'.format(dict1[each]))
        
    elif 65 <= float(each) < 70:
        n_size(400,400)
        new_im.save('C:/Users/36182/Desktop/new_plane/{0}.png'.format(dict1[each]))
        
    elif 70 <= float(each) < 75:
        n_size(500,500)
        new_im.save('C:/Users/36182/Desktop/new_plane/{0}.png'.format(dict1[each]))
        
    elif 75 <= float(each) < 80:
        n_size(600,600)
        new_im.save('C:/Users/36182/Desktop/new_plane/{0}.png'.format(dict1[each]))
        
    else:
        print("error")
        



import re


def plt_images_wall(img_path):
    imgs_path = []
    imgs_name = os.listdir(img_path)

    for img in imgs_name:
        imgs_path.append(os.path.join(img_path + "/", img))

    if int(len(imgs_path) / 4) != 0:   # 想要显示多行图片更改一下就可以

        for i in range(len(imgs_path)):
            print(int(str(4) + str(int(len(imgs_path) / 4)) + str(i + 1)))
			# 引入正则是为了解决浮点数的错误问题
            tmp = str(int(len(imgs_path) / 4))
            tmp = re.match("[0-9]", tmp)
            tmp = tmp.string

            plt.subplot(int(str(4) + str(tmp) + str(i + 1)))
            plt.title("image" + str((i + 1)))
            plt.axis("on")   # 打开坐标轴
            plt.imshow(Image.open(imgs_path[i]))
        plt.savefig("plt_wall.jpg")

    plt.show()

if __name__ == "__main__":
    plt_images_wall("new_plane") 

plt_images_wall('new_plane')  #此处调用函数，输入'文件夹名称'  
# new_plane文件夹里为 之前 for循环导入的飞机图

os.remove('C:/Users/36182/Desktop/new_plane')
#remove the file)




