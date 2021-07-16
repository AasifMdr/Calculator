from _ast import Lambda
from tkinter import *

root = Tk()
root.configure(bg='black')

# Title of the project

root.title('Basic Calculator')
root.iconbitmap('E:/calc.ico')

# interpreting the entry box

e = Entry(
    root,
    width=25,
    borderwidth=5,
    font=('courier', 30),
    fg='white',
    bg='black',
    )
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


# button click function

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))  # adding two strings


# equals to function

def button_equal():
    cal = str(e.get())  # store value of entry in cal
    total = eval(cal)  # runs the python which is passed as an argument
    e.delete(0, END)  # deletes the value in entry
    e.insert(0, total)  # inserts the value in entry


# clear function

def clear_button():
    e.delete(0, END)  # clears entry in the screen


# Defining and arranging the buttons in the screen

button_0 = Button(
    root,
    text='0',
    command=lambda : button_click(0),
    font=('courier', 30),
    fg='white',
    bg='black',
    activebackground='black',
    activeforeground='white',
    bd=0,
    )
button_0.grid(row=5, column=1, ipadx=40, ipady=20)

button_1 = Button(
    root,
    text='1',
    command=lambda : button_click(1),
    font=('courier', 30),
    fg='white',
    bg='black',
    activebackground='black',
    activeforeground='white',
    bd=0,
    )
button_1.grid(row=3, column=0, ipadx=40, ipady=20)

button_2 = Button(
    root,
    text='2',
    command=lambda : button_click(2),
    font=('courier', 30),
    fg='white',
    bg='black',
    activebackground='black',
    activeforeground='white',
    bd=0,
    )
button_2.grid(row=3, column=1, ipadx=40, ipady=20)

button_3 = Button(
    root,
    text='3',
    command=lambda : button_click(3),
    font=('courier', 30),
    fg='white',
    bg='black',
    activebackground='black',
    activeforeground='white',
    bd=0,
    )
button_3.grid(row=3, column=2, ipadx=40, ipady=20)

button_4 = Button(
    root,
    text='4',
    command=lambda : button_click(4),
    font=('courier', 30),
    fg='white',
    bg='black',
    activebackground='black',
    activeforeground='white',
    bd=0,
    )
button_4.grid(row=2, column=0, ipadx=40, ipady=20)

button_5 = Button(
    root,
    text='5',
    command=lambda : button_click(5),
    font=('courier', 30),
    fg='white',
    bg='black',
    activebackground='black',
    activeforeground='white',
    bd=0,
    )
button_5.grid(row=2, column=1, ipadx=40, ipady=20)

button_6 = Button(
    root,
    text='6',
    command=lambda : button_click(6),
    font=('courier', 30),
    fg='white',
    bg='black',
    activebackground='black',
    activeforeground='white',
    bd=0,
    )
button_6.grid(row=2, column=2, ipadx=40, ipady=20)

button_7 = Button(
    root,
    text='7',
    command=lambda : button_click(7),
    font=('courier', 30),
    fg='white',
    bg='black',
    activebackground='black',
    activeforeground='white',
    bd=0,
    )
button_7.grid(row=1, column=0, ipadx=40, ipady=20)

button_8 = Button(
    root,
    text='8',
    command=lambda : button_click(8),
    font=('courier', 30),
    fg='white',
    bg='black',
    activebackground='black',
    activeforeground='white',
    bd=0,
    )
button_8.grid(row=1, column=1, ipadx=40, ipady=20)

button_9 = Button(
    root,
    text='9',
    command=lambda : button_click(9),
    font=('courier', 30),
    fg='white',
    bg='black',
    activebackground='black',
    activeforeground='white',
    bd=0,
    )
button_9.grid(row=1, column=2, ipadx=40, ipady=20)

button_add = Button(
    root,
    text='+',
    command=lambda : button_click('+'),
    font=('courier', 30),
    fg='yellow',
    bg='black',
    activebackground='black',
    activeforeground='yellow',
    bd=0,
    )
button_add.grid(row=5, column=3, ipadx=40, ipady=20)

button_equal = Button(
    root,
    text='=',
    command=button_equal,
    font=('courier', 30),
    fg='yellow',
    bg='black',
    activebackground='black',
    activeforeground='yellow',
    bd=0,
    )
button_equal.grid(row=6, column=2, columnspan=2, ipadx=110, ipady=8)

button_clear = Button(
    root,
    text='C',
    command=clear_button,
    font=('courier', 30),
    fg='yellow',
    bg='black',
    activebackground='black',
    activeforeground='yellow',
    bd=0,
    )
button_clear.grid(row=1, column=3, ipadx=40, ipady=30)

button_sub = Button(
    root,
    text='-',
    command=lambda : button_click('-'),
    font=('courier', 30),
    fg='yellow',
    bg='black',
    activebackground='black',
    activeforeground='yellow',
    bd=0,
    )
button_sub.grid(row=3, column=3, ipadx=40, ipady=30)

button_mul = Button(
    root,
    text='x',
    command=lambda : button_click('*'),
    font=('courier', 30),
    fg='yellow',
    bg='black',
    activebackground='black',
    activeforeground='yellow',
    bd=0,
    )
button_mul.grid(row=2, column=3, ipadx=40, ipady=31)

button_div = Button(
    root,
    text='/',
    command=lambda : button_click('/'),
    font=('courier', 30),
    fg='yellow',
    bg='black',
    activebackground='black',
    activeforeground='yellow',
    bd=0,
    )
button_div.grid(row=5, column=0, ipadx=40, ipady=30)

button_mod = Button(
    root,
    text='MOD',
    command=lambda : button_click('%'),
    font=('courier', 30),
    fg='yellow',
    bg='black',
    activebackground='black',
    activeforeground='yellow',
    bd=0,
    )
button_mod.grid(row=6, column=0, ipadx=40, ipady=30)

button_power = Button(
    root,
    text='^',
    command=lambda : button_click('**'),
    font=('courier', 30),
    fg='yellow',
    bg='black',
    activebackground='black',
    activeforeground='yellow',
    bd=0,
    )
button_power.grid(row=5, column=2, ipadx=40, ipady=30)

button_dot = Button(
    root,
    text='.',
    command=lambda : button_click('.'),
    font=('courier', 30),
    fg='yellow',
    bg='black',
    activebackground='black',
    activeforeground='yellow',
    bd=0,
    )
button_dot.grid(row=6, column=1, ipadx=50, ipady=8)

mainloop()
