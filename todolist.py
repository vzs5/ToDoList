# testing "To Do List"
# by vzs
from tkinter import *
from tkinter import messagebox
import datetime as dt
import tkinter as tk
from tkinter import ttk
from time import strftime

#WarningBox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Uwaga", "Wpisz Zadanie.")

def deleteTask():
    lb.delete(ANCHOR)

#Okno

ws = Tk()
ws.geometry('500x520+200+100')
ws.title('To Do List')
ws.config(bg='#355E5B')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

#Data & Czas

date = dt.datetime.now()

label = Label(
    ws,
    text=f"{date:%A, %B %d, %Y: %H:%M %p}",
    font="Calibri, 20",
    background='black',
    foregroun='red',
    
)

label.pack(pady=20)



#Listbox

lb = Listbox(
    frame,
    width=35,
    height=10,
    font=('arial', 14),
    bd=0,
    fg='#660066',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

#tasklist

task_list = ()




for item in task_list:
    lb.insert(END, item)

#Scrollbar

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

#Wpisywarka6

my_entry = Entry(
    ws,
    font=('arial', 24),
    width="26",
    )

my_entry.pack(pady=20)

#Przycisk 1

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='DODAJ ZADANIE',
    font=('arial, 14'),
    bg='#808080',
    padx=10,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

#Przycisk 2

delTask_btn = Button(
    button_frame,
    text='USUŃ ZADANIE',
    font=('arial 14'),
    bg='#808080',
    padx=10,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()