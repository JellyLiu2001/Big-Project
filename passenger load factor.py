# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:34:46 2021

@author: 36182
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 11 11:54:28 2021

@author: 36182
"""
import xlrd
import numpy as np


T_sheet = xlrd.open_workbook("new data for graph.xlsx")#path
xl_sheet = T_sheet.sheet_by_index(0)
T_date = xl_sheet.row_values(1)#date
T_income = xl_sheet.row_values(2)#income
T_psrate = xl_sheet.row_values(3)#passenger load factor
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



import os
from PIL import Image       
im = Image.open('images\plane1.png') #open the image of the plane
print(im.size)#get the size of the image, whcihc is （500，500）at the beginning

pix = im.load()#pixel
width = im.size[0] #get the width
height = im.size[1] #get the height

def n_size(x,y):  #create a function to resize the image
    global new_im   #change the variable to globale variable
    new_im = im.resize((x,y))   #resize the image
    return new_im


os.mkdir('C:/Users/36182/Desktop/new_plane')#create a file

for each in dict1.keys():    #use for loop to change the size of the image according to the load factor
    if 50 <= float(each) < 55:
        n_size(100,100)          
        new_im.save('C:/Users/36182/Desktop/new_plane/{0}.png'.format(dict1[each])) #use foramt to name the image with the date   
        #save the image in a folder
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
        #the images are named with the date(month.week)
#===============================================================================

import tkinter as tk  # import tkinter
 
# step1: create a window
window = tk.Tk()
#name the window
window.title('passenger load factor')
 
# set the size of the window 
window.geometry('500x300')  #length x width
window.resizable(True,True)  #the window can be resizable


window.columnconfigure(0, weight = 1)
window.rowconfigure(0, weight = 1)

# step2: labels
picture = tk.PhotoImage(file = 'C:/Users/36182/Desktop/new_plane/2.1.png') 
Lab = tk.Label(window, image = picture)
Lab.grid(column=0, row=1) #set location
#label the image(initial image)

lb = tk.Label(window, bg='pink', fg='white',font=('Arial', 14), width=13, text = 'month.week')
lb.grid(column=0, row=30)
#label the text(initial text)

# step3: set listbox
lists = (date1) #give value (the 'tens' means month, the 'ones' means which week in this month) to the lists
lists_var = tk.StringVar(value = lists)

listbox = tk.Listbox(window, listvariable = lists_var, height = 8) #set the listbox
listbox.delete(0) #remove the first element because it contains'['
listbox.delete(22) #remove the last element becayse it contains ']'
listbox.insert(0,'1.1') #add 1.1 to the first
listbox.insert(23,'8.3') #add 8.3 to the last
listbox.grid(column=0, row=100)






def items_selected():
    selected_indices = listbox.curselection()  
    selected_value = listbox.get(selected_indices[0])  #give the selected value in the listbox to the varialble: selected_value
    print(selected_value)
    lb['text'] = selected_value   #change the labeled text to the selected value
    
    
    global file_name
    file_name = 'C:/Users/36182/Desktop/new_plane/'+selected_value+'.png'  
    global picture
    global Lab
    picture = tk.PhotoImage(file = file_name) 
    Lab = tk.Label(window, image = picture) 
    Lab.grid(column=0, row=1)
#change the displayed image, which file name is corresponding to the selected value(month.week)
    print(file_name)

button = tk.Button(window, text='confirm', width=20, height=1, command = items_selected)
button.grid(column=0, row=60)



#listbox.bind('<<ListboxSelect>>', items_selected) #bind the function to the listbox

window.mainloop()