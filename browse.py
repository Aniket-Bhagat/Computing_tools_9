from Tkinter import *
import tkFileDialog

def browseQuery(e):
	filename = tkFileDialog.askopenfilename(title = "Select Query sequence file",filetypes = (("fasta files","*.fasta"),("all files","*.*")))
	#Using try in case user types in unknown file or closes without choosing a file.
	try:
		with open(filename,'r') as f:
			content = f.read()
			e.delete(0, END)
			e.insert(0, content)
	except:
		print("No file exists")

def browseRef(e):
	filename = tkFileDialog.askopenfilename(title = "Select Refrence sequence file",filetypes = (("fasta files","*.fasta"),("all files","*.*")))
	#Using try in case user types in unknown file or closes without choosing a file.
	try:
		with open(filename,'r') as f:
			content = f.read()
			e.delete(0, END)
			e.insert(0, content)
	except:
		print("No file exists")


