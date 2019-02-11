from Tkinter import *
from tkMessageBox import *

def confirm_answer():
	showerror('Error Window','Sorry pal, wrong Answer')
def byebye():
	if askeysno('Confirmation Window','Are you sure you wanna quite?'):
		showinfo('Positive','Hope you enjoyed it. See ya..!!')
	else:
		showinfo('Negative','Bravo.! You are not a quiter')

Button(text='Eureka.!!',command=confirm_answer).pack(side=LEFT)
Button(text='Quit',command=byebye).pack(side=RIGHT)

mainloop()