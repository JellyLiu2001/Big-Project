import os
from tkinter import *
root = Tk()
def project_chart():
    os.system("python project数据图表.py")
def data_pic():
    os.system("python PSloadcoloured.py")
def all():
    os.system("python project数据图表.py")
    os.system("python PSloadcoloured.py")
    os.system("web.html")
def html():
    os.system("web.html")

text=Text(root,width=100,height=3,fg='black')
text.insert(1.0,'This is a group of UOB student that working with a big project to simulate the covid-19.')
Button(root,text='Chart',anchor='c',bg='blue',fg='white',padx=100,pady=20,borderwidth=10,relief='ridge',compound='bottom',command=project_chart).pack()
Button(root,text='Data picture',anchor='c',bg='red',fg='white',padx=80,pady=20,borderwidth=10,relief='ridge',compound='bottom',command=data_pic).pack()
Button(root,text='All',anchor='c',bg='green',fg='white',padx=110,pady=20,borderwidth=10,relief='ridge',compound='bottom',command=all).pack()
Button(root,text='WEB',anchor='c',bg='green',fg='white',padx=105,pady=20,borderwidth=10,relief='ridge',compound='bottom',command=html).pack()
text.pack()
root.mainloop()