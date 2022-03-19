import tkinter as tk
from tkinter import *


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(490,183))
        self.master.title('Check files')
        self.master.config(bg = 'lightgray')

        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse1.grid(row=0, column=0, padx=(20,0), pady=(40,0))

        self.txtEntry1 = Entry(self.master, text='', width = 55)
        self.txtEntry1.grid(row=0, column=1, columnspan = 2, padx=(20,0), pady=(40,0))

        self.btnBrowse2 = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse2.grid(row=1, column=0, padx=(20,0), pady=(10,0))

        self.txtEntry2 = Entry(self.master, text='', width = 55)
        self.txtEntry2.grid(row=1, column=1, columnspan = 2, padx=(20,0), pady=(10,0))

        self.btnCheck = Button(self.master, text="Check for files...", width=12, height=2)
        self.btnCheck.grid(row=2, column=0, padx=(20,0), pady=(10,0))

        self.btnClose = Button(self.master, text="Close Program", width=12, height=2)
        self.btnClose.grid(row=2, column=2, padx=(0,0), pady=(10,0), sticky=E)




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
