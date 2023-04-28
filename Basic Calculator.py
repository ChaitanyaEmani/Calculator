from tkinter import *
import string
root = Tk()
root.title("Basic Calculator")
e=Entry(root,width = 70,borderwidth=5,bg = "white",fg = "black")
e.grid(row = 0,column=0,columnspan = 30,padx=10,pady=10)


def buttonClick(Number):
    currentNumber = e.get()
    e.delete(0, END)
    e.insert(0,str(currentNumber)+str(Number))


def buttonAdd():
    FirstNumber = e.get()
    global f_num
    global maths
    maths = "Addition"
    f_num = float(FirstNumber)
    e.delete(0, END)
def buttonSubtraction():
    FirstNumber = e.get()
    global f_num
    global maths
    maths = "Subtraction"
    f_num = float(FirstNumber)
    e.delete(0, END)

def buttonMultipication():
    FirstNumber = e.get()
    global f_num
    global maths
    maths = "Multiplication"
    f_num = float(FirstNumber)
    e.delete(0, END)
def buttonDivision():
    FirstNumber = e.get()
    global f_num
    global maths
    maths = "Division"
    f_num = float(FirstNumber)
    e.delete(0, END)

def buttonModulo():
    FirstNumber = e.get()
    global f_num
    global maths
    maths = "Modulus"
    f_num = float(FirstNumber)
    e.delete(0, END)

def buttonfloorDiv():
    FirstNumber = e.get()
    global f_num
    global maths
    maths = "Floor Division"
    f_num = float(FirstNumber)
    e.delete(0, END)

def buttonIncrement():
    FirstNumber = e.get()
    global f_num
    global maths
    maths = "Increment"
    f_num = float(FirstNumber)
    e.delete(0, END)

def buttonDecrement():
    FirstNumber = e.get()
    global f_num
    global maths
    maths = "Decrement"
    f_num = float(FirstNumber)
    e.delete(0, END)
def buttonEqual():
    Second_Number  = e.get()
    e.delete(0,END)
    if maths == "Addition":
        e.insert(0,f_num+float(Second_Number))
    if maths == "Subtraction":
        e.insert(0,f_num-float(Second_Number))
    if maths == "Multiplication":
        e.insert(0,f_num*float(Second_Number))
    if maths == "Division":
        e.insert(0,f_num/float(Second_Number))
    if maths == "Modulus":
        e.insert(0,f_num%float(Second_Number))
    if maths == "Floor Division":
        e.insert(0,f_num//float(Second_Number))
    if maths == "Increment":
        e.insert(0,f_num+1)
    if maths == "Decrement":
        e.insert(0,f_num-1)
def buttonClear():
    e.delete(0,END)
b0 = Button(root,text = "0",padx = 40,pady = 20,command = lambda: buttonClick(0),fg = "black",bg = "white")
b1 = Button(root,text = "1",padx = 40,pady = 20,command = lambda: buttonClick(1),fg = "black",bg = "white")
b2 = Button(root,text = "2",padx = 40,pady = 20,command = lambda: buttonClick(2),fg = "black",bg = "white")
b3 = Button(root,text = "3",padx = 40,pady = 20,command = lambda: buttonClick(3),fg = "black",bg = "white")
b4 = Button(root,text = "4",padx = 40,pady = 20,command = lambda: buttonClick(4),fg = "black",bg = "white")
b5 = Button(root,text = "5",padx = 40,pady = 20,command = lambda: buttonClick(5),fg = "black",bg = "white")
b6 = Button(root,text = "6",padx = 40,pady = 20,command = lambda: buttonClick(6),fg = "black",bg = "white")
b7 = Button(root,text = "7",padx = 40,pady = 20,command = lambda: buttonClick(7),fg = "black",bg = "white")
b8 = Button(root,text = "8",padx = 40,pady = 20,command = lambda: buttonClick(8),fg = "black",bg = "white")
b9 = Button(root,text = "9",padx = 40,pady = 20,command = lambda: buttonClick(9),fg = "black",bg = "white")
add = Button(root,text = "+",padx= 40,pady=20,command = buttonAdd,fg = "white",bg = "#66b3ff")
sub = Button(root,text = "-",padx= 40,pady=20,command=buttonSubtraction,fg = "white",bg = "#66b3ff")
modulo = Button(root,text = "%",padx= 40,pady=20,command=buttonModulo,fg = "white",bg = "#66b3ff")
floorDiv = Button(root,text = "//",padx= 40,pady=20,command=buttonfloorDiv,fg = "white",bg = "#66b3ff")
mul = Button(root,text = "x",padx= 40,pady=20,command=buttonMultipication,fg = "white",bg = "#66b3ff")
div = Button(root,text = "÷",padx= 40,pady=20,command=buttonDivision,fg = "white",bg = "#66b3ff")
equal = Button(root,text = "=",padx = 40,pady = 20,command = buttonEqual,fg = "white",bg = "#66b3ff")
clear = Button(root,text = "⌫",padx = 40,pady = 20,command = buttonClear,fg = "white",bg = "#66b3ff")
increment = Button(root,text = "++",padx = 40,pady = 20,command = buttonIncrement,fg = "white",bg = "#66b3ff")
Decrement = Button(root,text = "--",padx = 40,pady = 20,command = buttonDecrement,fg = "white",bg = "#66b3ff")
b0.grid(row= 4,column=1)
b1.grid(row= 3,column=0)
b2.grid(row= 3,column=1)
b3.grid(row= 3,column=2)
b4.grid(row= 2,column=0)
b5.grid(row= 2,column=1)
b6.grid(row= 2,column=2)
b7.grid(row= 1,column=0)
b8.grid(row= 1,column=1)
b9.grid(row= 1,column=2)
add.grid(row= 1,column=3)
sub.grid(row= 2,column=3)
mul.grid(row= 3,column=3)
div.grid(row= 4,column=3)
equal.grid(row = 4,column = 2)
clear.grid(row=4,column= 0)
modulo.grid(row = 1 ,column = 4 )
floorDiv.grid(row = 2 ,column = 4)
increment.grid(row = 3,column = 4)
Decrement.grid(row = 4,column = 4)
root.mainloop()