import numpy as np
import xlrd#导入Excel库
T_sheet = xlrd.open_workbook("T_data数据汇总.xlsx")#设置表格路径
xl_sheet = T_sheet.sheet_by_index(0)#设置表格中的sheet
T_date = xl_sheet.row_values(1)#总日期
T_income = xl_sheet.row_values(2)#总收入
T_psrate = xl_sheet.row_values(3)#总客座率
T_outcome = xl_sheet.row_values(4)#总支出
T_flight = xl_sheet.row_values(5)#总航班数
T_sick = xl_sheet.row_values(6)#总生病人数
T_new = xl_sheet.row_values(7)#新增感染人数
# print(T_date,T_income,T_psrate,T_outcome,T_flight,T_sick,T_new)#打印所有数据


# insert 'plane' image for map animation 
from PIL import Image
myImage = Image.open("images\green.jpg");
# myImage.show()

# identify the cases of the day by three classes (test)
int_new = 1
# print(T_new[int_new])
if T_new[int_new] == 0:
    im = Image.open('images\plane1.jpg')
    # print("无")
    # colour = green
elif 0 < T_new[int_new] <=5:
    im = Image.open('images\green.jpg')
    # print("有")
    # colour = orange
else:
    im = Image.open('images\red.jpg')
    # print("多")
    # colour = red
# int_new = int_new + 1    

# # print(T_new[int_new])
# if T_new[int_new] == 0:
#     print("无")
# elif 0 < T_new[int_new] <=5:
#     print("有")
# else:
#     print("多")
# int_new = int_new + 1    

# # print(T_new[int_new])
# # print(int_new)
# if T_new[int_new] == 0:
#     print("无")
# elif 0 < T_new[int_new] <=5:
#     print("有")
# else:
#     print("多")


# change colour of 'plane' depends on cases on the day

psrate=np.array(T_psrate[1:]) #remove the string in excel
print(psrate)
date1=np.array(T_date[1:])
print(date1)

dict1=dict(zip(psrate,date1))#create a dictionary
print(dict1)


import os
from PIL import Image       
# im = Image.open('images\green.jpg') #open the image of the plane
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




































































