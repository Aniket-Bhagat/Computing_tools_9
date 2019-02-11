from Tkinter import *

window = Tk()
window.geometry('350x200')
window.title('Demo of the Button Widget')

b1 = Button(window, text='Show').pack()
b2 = Button(window, text='Exit',command='exit').pack()

window.mainloop()