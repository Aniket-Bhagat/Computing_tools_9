from Tkinter import *
import tkFileDialog,ttk

root = Tk()

def browsefunc():
    filename = tkFileDialog.askopenfilename(title = "Select Query sequence file",filetypes = (("fasta files","*.fasta"),("all files","*.*")))
    # pathlabel.config(text=filename)
    # print (filename)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(filename,'r') as f:
            print(f.read())
    except:
        print("No file exists")


browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.pack()

pathlabel = Label(root)
pathlabel.pack()
root.mainloop()