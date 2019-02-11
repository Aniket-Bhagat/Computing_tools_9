from Tkinter import *

window = Tk()
window.geometry('350x200')
window.title('Demo of the Button Widget')

# b1 = Button(window, text='Show').pack()
# b2 = Button(window, text='Exit',command='exit').pack()


class MyGui:
	def __init__(self,parent):
		f=Frame(parent)
		f.pack()
		self.b1=Button(f,text='Greet',fg='blue',command=self.func)
		self.b1.pack(side=LEFT)
		self.b2=Button(f,text='Quit',fg='red',command='exit')
		self.b2.pack(side=RIGHT)
	def func(self):
		print 'hello world'

app=MyGui(window)
window.mainloop()