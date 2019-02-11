from Tkinter import *
import Tkinter, tkFileDialog

root = Tk()

root = tkFileDialog.askopenfilename(filetypes = (('Text files','*.txt'),('all files','*.*')))
root.mainloop()