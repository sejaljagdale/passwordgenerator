#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#password generator
import random
import pyperclip
from tkinter import *
from tkinter.ttk import *
 
# Function for calculation of password
 
 
def low():
    entry.delete(0, END)
 
    # Get the length of password
    length = var1.get()
 
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""
 
    # if strength selected is low
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password
 
    # if strength selected is medium
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password
 
    # if strength selected is strong
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Please choose an option")
 
 
# Function for generation of password
def generate():
    password1 = low()
    entry.insert(10, password1)
 
 
# Function for copying password to clipboard
def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)
 
 
# Main Function
 
# create GUI window
root = Tk()
var = IntVar()
var1 = IntVar()
 
# Title of your GUI window
root.title("Random Password Generator")
 
# create label and entry to show
# password generated
Random_password = Label(root, text="Password")
Random_password.grid(row=0)
Random_password.place(x=50,y=50)

entry = Entry(root)
entry.grid(row=0, column=1)
entry.place(x=200,y=50)

 
# create label for length of password
c_label = Label(root, text="Length")
c_label.grid(row=1)
c_label.place(x=50,y=100)
 
# create Buttons Copy which will copy
# password to clipboard and Generate
# which will generate the password
copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=0, column=2)
copy_button.place(x=50,y=150)


generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)
generate_button.place(x=150,y=150)
 
# Radio Buttons for deciding the
# strength of password
# Default strength is Medium
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_low.place(x=250,y=150)

radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E')
radio_middle.place(x=250,y=180)

radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')
radio_strong.place(x=250,y=210)

combo = Combobox(root, textvariable=var1)
 
# Combo Box for length of your password
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)
combo.place(x=200,y=100)

root.configure(background="light pink") 

root.geometry("450x300+100+50")
 
# start the GUI
root.mainloop()

