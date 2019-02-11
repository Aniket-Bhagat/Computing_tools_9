# import sys
# import ttk
# from Tkinter import *

# mGui = Tk()

# mGui.geometry('450x450')
# mGui.title('Hanix Downloader')

# mpb = ttk.Progressbar(mGui,orient ="horizontal",length = 200, mode ="indeterminate")
# mpb.pack()
# mpb["maximum"] = 100
# mpb["value"] = 10

# mGui.mainloop()

# ------------------------------------------------------------------------------------------------- #

# from Tkinter import *
# import ttk

# root = Tk()
    
# def start():
#     pb = ttk.Progressbar(root, orient='horizontal', mode='indeterminate')
#     pb.pack(expand=True, fill=BOTH, side=TOP)
#     pb.start(5)

# button = Button(root, text="start", command=start)
# button.pack()

# root.mainloop()

# ------------------------------------------------------------------------------------------------- #

# try:
#   import Tkinter              # Python 2
#   import ttk
# except ImportError:
#   import tkinter as Tkinter   # Python 3
#   import tkinter.ttk as ttk


# def main():

#   root = Tkinter.Tk()

#   ft = ttk.Frame()
#   fb = ttk.Frame()

#   ft.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
#   fb.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)

#   pb_hd = ttk.Progressbar(ft, orient='horizontal', mode='determinate')
#   pb_hD = ttk.Progressbar(ft, orient='horizontal', mode='indeterminate')
#   pb_vd = ttk.Progressbar(fb, orient='vertical', mode='determinate')
#   pb_vD = ttk.Progressbar(fb, orient='vertical', mode='indeterminate')

#   pb_hd.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
#   pb_hD.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
#   pb_vd.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.LEFT)
#   pb_vD.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.LEFT)

#   pb_hd.start(50)
#   pb_hD.start(50)
#   pb_vd.start(50)
#   pb_vD.start(50)

#   root.mainloop()


# if __name__ == '__main__':
#   main()