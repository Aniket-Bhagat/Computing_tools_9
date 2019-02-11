#!/usr/bin/env python
from Tkinter import *
import tkFileDialog,ttk
from EMBOSS import DoEmboss as DE 			# User defind module
from translate import GetProtein as GP,CompareProtein as CP 		# User defind module

root = Tk()
root.title('SNV Detection Tool')
root.geometry('720x405')
#--------------------------------------------------------------------------------------------#
label1 = ttk.Label(root, text ="SNV Detection Tool",foreground="red",font=("Algerian", 20))
label1.pack()
#--------------------------------------------------------------------------------------------#

def browseQuery():
	filename = tkFileDialog.askopenfilename(title = "Select Query sequence file",
		filetypes = (("fasta files","*.fasta"),("all files","*.*")))
	#Using try in case user types in unknown file or closes without choosing a file.
	try:
		with open(filename,'r') as f:
			content = f.read()
			e1.delete('1.0', END)
			e1.insert('1.0', content)
	except:
		pass

label2 = Label(root,text="Input Query Sequence (fasta format) :",anchor=W)
label2.pack(side="top", anchor="w")

e1 = Text(root,height=5,width=80)
e1.insert(END, '')
e1.pack(side="top",anchor="w")

browsebutton = Button(root, text="Browse", command=browseQuery)
browsebutton.pack(anchor="w")
#--------------------------------------------------------------------------------------------#

def browseRef():
	filename = tkFileDialog.askopenfilename(title = "Select Refrence sequence file",filetypes = (("fasta files","*.fasta"),("all files","*.*")))
	#Using try in case user types in unknown file or closes without choosing a file.
	try:
		with open(filename,'r') as f:
			content = f.read()
			e2.delete('1.0', END)
			e2.insert('1.0', content)
	except:
		pass

label3 = Label(root,text="Input Refrence Sequence (fasta format) :",anchor=W)
label3.pack(side="top", anchor="w")

e2 = Text(root,height=5,width=80)
e2.insert(END, '')
e2.pack(side="top",anchor="w")

browsebutton = Button(root, text="Browse", command=browseRef)
browsebutton.pack(anchor="w")
#--------------------------------------------------------------------------------------------#

def LoadEmboss():
	with open('alpha.faa','w') as q:
		q.write(e1.get('0.1',END))
		q.close()
	with open('beta.faa','w') as r:
		r.write(e2.get('0.1',END))
		r.close()

	result.configure(text = DE())

Emboss = Button(root, text="EMBOSS", command=LoadEmboss)
Emboss.pack(anchor="w")

result = Label(root, text = 'Result')
result.pack(side = 'bottom', anchor = 'w')

#---------------------------------------------------------------------------------------------#

def ShowProtein():
	query_N = e1.get('0.1',END)
	ref_N = e2.get('0.1',END)
	
	query_P = GP(query_N)
	ref_P = GP(ref_N)

	result2.configure(text = CP(query_P,ref_P))

ProtAnalysis = Button(root, text="Analysis", command=ShowProtein)
ProtAnalysis.pack(anchor="w")

result2 = Label(root, text = 'Result2')
result2.pack(side = 'bottom', anchor = 'w')
#---------------------------------------------------------------------------------------------#

root.mainloop()