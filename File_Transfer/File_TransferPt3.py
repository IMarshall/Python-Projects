import shutil
import os
import datetime
from datetime import timedelta
import tkinter as tk
from tkinter import *
from tkinter import filedialog


class ParentWindow(Frame):
    
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(490,183))
        self.master.title('Check files')
        self.master.config(bg = 'lightgray')

        self.btnBrowse1 = Button(self.master, text="Browse...", command=lambda: self.browse(self.sourcePath), width=12, height=1)
        self.btnBrowse1.grid(row=0, column=0, padx=(20,0), pady=(40,0))

        self.sourcePath = Label(self.master, text='', width = 45)
        self.sourcePath.grid(row=0, column=1, columnspan = 2, padx=(20,0), pady=(40,0))

        self.btnBrowse2 = Button(self.master, text="Browse...", command=lambda: self.browse(self.destPath), width=12, height=1)
        self.btnBrowse2.grid(row=1, column=0, padx=(20,0), pady=(10,0))

        self.destPath = Label(self.master, text='', width = 45)
        self.destPath.grid(row=1, column=1, columnspan = 2, padx=(20,0), pady=(10,0))

        self.btnCheck = Button(self.master, text="File Check", command=lambda: self.fileCheck(), width=12, height=2)
        self.btnCheck.grid(row=2, column=0, padx=(20,0), pady=(10,0))

        self.btnClose = Button(self.master, text="Close Program", width=12, height=2)
        self.btnClose.grid(row=2, column=2, padx=(0,0), pady=(10,0), sticky=E)

    def browse(self, line):
        path = tk.filedialog.askdirectory()
        line.configure(text=path)

    def fileCheck(self):
        ##set where the source of the files are
        source = self.sourcePath.cget("text")+"/"

        ##set the destination path
        destination = self.destPath.cget("text")
        files = os.listdir(source)
        today = datetime.datetime.now()
        yesterday = today - timedelta(days=1)

        for i in files:
            modTime = datetime.datetime.fromtimestamp(os.path.getmtime(source+i))
            if modTime < yesterday:
                print('This file is old. Didn\'t do anything')
            else:
                shutil.copy(source+i,destination)
                print('This file is new. Copied to destination.')
        

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()


