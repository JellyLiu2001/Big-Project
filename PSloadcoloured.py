
import tkinter as tk  # import tkinter
import xlrd
import numpy as np
import os
from PIL import Image


xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True

T_sheet = xlrd.open_workbook("new data for graph.xlsx")  # path
# T_sheet = xlrd.open_workbook("T_data数据汇总.xlsx")#path
xl_sheet = T_sheet.sheet_by_index(0)
T_date = xl_sheet.row_values(1)  # date
T_income = xl_sheet.row_values(2)  # income
T_psrate = xl_sheet.row_values(3)  # passenger load factor
T_outcome = xl_sheet.row_values(4)  # outcome
T_flight = xl_sheet.row_values(5)  # number of flights
T_sick = xl_sheet.row_values(6)  # number of sickness people
T_new = xl_sheet.row_values(7)  # number of new cases

psrate = np.array(T_psrate[1:])  # remove the string in excel
print(psrate)
date1 = np.array(T_date[1:])
print(date1)
dict1 = dict(zip(psrate, date1))  # create a dictionary
print(dict1)
new = np.array(T_new[1:])
dict2 = dict(zip(date1, new))                                                  #Zhu: create another dictionary with new cases   

# print(dict2)
# print(dict2.values())

def select_image(value):                                                       #Zhu: conditions chosing images dependent on new cases from excel
    if value > 10:
        return './images/red.jpg'
    elif 0 < value <= 5:
        return 'images/yellow.jpg'
    elif 5 < value <= 15:
        return 'images/orange.jpg'
    return './images/green.jpg'
  
def n_size(x, y, img):  # create a function to resize the image                
    im = Image.open(img)                                                       #Zhu: combined function use to change size of picture with choseing image
    # pix = im.load()  # pixel
    # width = im.size[0]  # get the width
    # height = im.size[1]  # get the height
    new_im = im.resize((x, y))  # resize the image
    return new_im


if not os.path.exists('images/new_plane'):                                     #Zhu: use 'if not' to avoid error when repeatted running the code
    os.mkdir('images/new_plane')  # create a file

for each in dict1.keys(): # use for loop to change the size of the image according to the load factor

    img = select_image(dict2[dict1[each]])                                     #Zhu: chosing corresponsing image dependent on cases of the day 
    if 50 <= float(each) < 55:
        new_im = n_size(100, 100, img)
        # use foramt to name the image with the date
        new_im.save('images/new_plane/{0}.png'.format(dict1[each]))
        # save the image in a folder
    elif 55 <= float(each) < 60:
        new_im = n_size(200, 200, img)
        new_im.save('images/new_plane/{0}.png'.format(dict1[each]))

    elif 60 <= float(each) < 65:
        new_im = n_size(300, 300, img)
        new_im.save('images/new_plane/{0}.png'.format(dict1[each]))

    elif 65 <= float(each) < 70:
        new_im = n_size(400, 400, img)
        new_im.save('images/new_plane/{0}.png'.format(dict1[each]))

    elif 70 <= float(each) < 75:
        new_im = n_size(500, 500, img)
        new_im.save('images/new_plane/{0}.png'.format(dict1[each]))

    elif 75 <= float(each) < 80:
        new_im = n_size(600, 600, img)
        new_im.save('images/new_plane/{0}.png'.format(dict1[each]))

    else:
        print("error")
        # the images are named with the date(month.week)
# ===============================================================================


# step1: create a window
window = tk.Tk()
# name the window
window.title('passenger load factor')

# set the size of the window
window.geometry('500x300')  # length x width
window.resizable(True, True)  # the window can be resizable


window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# step2: labels
picture = tk.PhotoImage(file='images/new_plane/1.1.png')
Lab = tk.Label(window, image = picture)
Lab.grid(column=0, row=1)  # set location
# label the image(initial image)

                                                                               #Zhu: lable the annotation alongside simulated plane
lc = tk.Label(window, bg='lightgrey', fg='white', font=(
    'Arial', 14), width=13, text='Green: new case=0'"\n"'Yellow: 0<new case<=5'"\n"'Orange: 5<new case<=15'"\n"'Red: new case>15')
lc.grid(column=1, row=30)

lb = tk.Label(window, bg='pink', fg='white', font=(
    'Arial', 14), width=13, text='month.week')
lb.grid(column=0, row=30)
# label the text(initial text)

# step3: set listbox
# give value (the 'tens' means month, the 'ones' means which week in this month) to the lists
lists = (date1)
lists_var = tk.StringVar(value=lists)

listbox = tk.Listbox(window, listvariable=lists_var,
                     height=8)  # set the listbox
listbox.delete(0)  # remove the first element because it contains'['
listbox.delete(22)  # remove the last element becayse it contains ']'
listbox.insert(0, '1.1')  # add 1.1 to the first
listbox.insert(23, '8.3')  # add 8.3 to the last
listbox.grid(column=0, row=100)


def items_selected():
    selected_indices = listbox.curselection()
    # give the selected value in the listbox to the varialble: selected_value
    selected_value = listbox.get(selected_indices[0])
    print(selected_value)
    lb['text'] = selected_value  # change the labeled text to the selected value

    global file_name  # 同上，改new_plane前面的路径，改成自己桌面
    file_name = 'images/new_plane/'+selected_value+'.png'
    global picture
    global Lab
    picture = tk.PhotoImage(file=file_name)
    Lab = tk.Label(window, image=picture)
    Lab.grid(column=0, row=1)
# change the displayed image, which file name is corresponding to the selected value(month.week)
    print(file_name)


button = tk.Button(window, text='confirm', width=20,
                   height=1, command=items_selected)
button.grid(column=0, row=60)


# listbox.bind('<<ListboxSelect>>', items_selected) #bind the function to the listbox

window.mainloop()
