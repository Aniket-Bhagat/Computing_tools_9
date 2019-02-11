'''
from Tkinter import *

root = Tk()
text = Text(root)
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background = "yellow", foreground = "blue")
text.tag_config("start", background = "black", foreground = "green")
root.mainloop()
'''

#----------------------------------------------------------------------#
'''
from Tkinter import *
import ttk
import tkMessageBox
root = Tk()
tx = Text(root, background='white', font='Courier 12')
tx.grid(column=0, row=0, sticky=(N, W, E, S))
ybar = ttk.Scrollbar(root, orient=VERTICAL, command=tx.yview)
ybar.grid(column=1, row=0, sticky=(N, W, E, S))
xbar = ttk.Scrollbar(root, orient=HORIZONTAL, command=tx.xview)
xbar.grid(column=0, row=1, columnspan=2, sticky=(N, W, E, S))
tx["yscrollcommand"] = ybar.set
tx["xscrollcommand"] = xbar.set
tx.tag_config('hide', elide=1)
tx.tag_config('bold', font='Courier 12 bold')
lastplace=tx.index('1.0')
def boldit():
    global tx, lastplace
    nextplace = tx.search('[B]', lastplace, 'end')
    if nextplace:
        boldon = nextplace + ' +3c'
        tx.tag_add('hide', nextplace, boldon)
        boldoff = tx.search('[/B]', boldon, 'end')
        if boldoff:
            tx.tag_add('bold', boldon, boldoff) 
            codoff = boldoff + ' +4c'
            tx.tag_add('hide', boldoff, codoff)
        lastplace = codoff
        boldit()
    else:
        return
tx.insert('1.0', """When, in the course of [B]human events,[/B] it becomes [B]necessary[/B] for one people to [B]dissolve[/B] the political bands ...""")
boldit()        
root.mainloop()
'''

#-----------------------------------------------------------------------#

from Tkinter import *

master = Tk()

w = Text(master, height=1, borderwidth=0, background='lightgray')
w.insert(INSERT, """ACGCTGACGATTTTCGCGATCGGTAGCTAGCTACGACTT""")
w.pack()

x=[14,17]
for i in range(2):
    w.tag_add("here", "1."+str(x[i]-1), "1."+str(x[i]))
    # w.tag_add("start", "1.8", "1.13")
    w.tag_config("here", background = "red", foreground = "white")
    # w.tag_config("start", background = "green", foreground = "white")

w.configure(state="disabled")

# if tkinter is 8.5 or above you'll want the selection background
# to appear like it does when the widget is activated
# comment this out for older versions of Tkinter
# w.configure(inactiveselectbackground=w.cget("selectbackground"))

mainloop()
