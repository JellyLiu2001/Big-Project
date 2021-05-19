import os
from tkinter import *
root = Tk()
root.title('Indexes')
def project_chart():
    os.system("python Normalgraph.py")
def data_pic():
    os.system("python PSloadcoloured.py")
def animated():
    os.system("python animatedgraph.py")    
def all():
    os.system("python Normalgraph.py")
    os.system("python PSloadcoloured.py")
    os.system("python animatedgraph.py")
    os.system("web.html")

def html():
    os.system("web.html")

text=Text(root,width=100,height=3,fg='black')
text.insert(1.0,'This is a group of student in University Of Bristol that working with a big project to simulate the covid-19.')
Button(root,text='Chart',anchor='c',bg='blue',fg='white',padx=100,pady=20,borderwidth=10,relief='ridge',compound='bottom',command=project_chart).pack()
Button(root,text='Data picture',anchor='c',bg='red',fg='white',padx=80,pady=20,borderwidth=10,relief='ridge',compound='bottom',command=data_pic).pack()
Button(root,text='animated',anchor='c',bg='red',fg='white',padx=80,pady=20,borderwidth=10,relief='ridge',compound='bottom',command=animated).pack()
Button(root,text='All',anchor='c',bg='green',fg='white',padx=110,pady=20,borderwidth=10,relief='ridge',compound='bottom',command=all).pack()
Button(root,text='WEB',anchor='c',bg='green',fg='white',padx=105,pady=20,borderwidth=10,relief='ridge',compound='bottom',command=html).pack()
text.pack()
root.mainloop()