# Simple Calculator

from Tkinter import *

def Add():
	a = int(e1.get())
	b = int(e2.get())
	data = (a+b)
	result.configure(text = data)

def Subtract():
	a = int(e1.get())
	b = int(e2.get())
	data = (a-b)
	result.configure(text = data)

def Multiply():
	a = int(e1.get())
	b = int(e2.get())
	data = (a*b)
	result.configure(text = data)

def Divide():
	a = int(e1.get())
	b = int(e2.get())
	data = (a/b)
	result.configure(text = data)

master = Tk()
Label(master, text="First Number").grid(row=0)
Label(master, text="Last Number").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=5, column=0)
Button(master, text='Add', command=Add).grid(row=3, column=0)
Button(master, text='Subtract', command=Subtract).grid(row=3, column=1)
Button(master, text='Multiply', command=Multiply).grid(row=3, column=2)
Button(master, text='Divide', command=Divide).grid(row=3, column=3)

result = Label(master, text = '')
result.grid(row = 4, column = 0)
mainloop( )