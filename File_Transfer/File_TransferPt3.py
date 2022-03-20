import shutil
import os
import datetime
from datetime import timedelta
import tkinter as tk
from tkinter import *
from tkinter import filedialog

##Build GUI
class ParentWindow(Frame):
    
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(490,220))
        self.master.title('Check files')
        self.master.config(bg = 'lightgray')

        self.lblSource = tk.Label(self.master, text='Source:', bg='lightgray', width=30)
        self.lblSource.grid(row=0, column=0, columnspan=3, padx=(20,0), pady=(20,0))

        self.btnBrowse1 = Button(self.master, text="Browse...", command=lambda: self.browse(self.sourcePath), width=12, height=1)
        self.btnBrowse1.grid(row=1, column=0, padx=(20,0), pady=(10,0))

        self.sourcePath = Label(self.master, text='', width = 45)
        self.sourcePath.grid(row=1, column=1, columnspan = 2, padx=(20,0), pady=(10,0))

        self.lblDest = tk.Label(self.master, text='Destination:', bg='lightgray', width=30)
        self.lblDest.grid(row=2, column=0, columnspan=3, padx=(20,0), pady=(10,0))

        self.btnBrowse2 = Button(self.master, text="Browse...", command=lambda: self.browse(self.destPath), width=12, height=1)
        self.btnBrowse2.grid(row=3, column=0, padx=(20,0), pady=(10,0))

        self.destPath = Label(self.master, text='', width = 45)
        self.destPath.grid(row=3, column=1, columnspan = 2, padx=(20,0), pady=(10,0))

        self.btnCheck = Button(self.master, text="File Check", command=lambda: self.fileCheck(), width=12, height=2)
        self.btnCheck.grid(row=4, column=0, padx=(20,0), pady=(10,0))

        self.btnClose = Button(self.master, text="Close Program", command=lambda: self.ask_quit(), width=12, height=2)
        self.btnClose.grid(row=4, column=2, padx=(0,0), pady=(10,0), sticky=E)

    def browse(self, line): ##open and select directories
        path = tk.filedialog.askdirectory(initialdir = './')
        line.configure(text=path)

    def fileCheck(self):
        ##set where the source of the files are
        source = self.sourcePath.cget("text")
        source = source.strip()

        ##set the destination path
        destination = self.destPath.cget("text")
        destination = destination.strip()

        if len(source) == 0 or len(destination) == 0: ##Check to make sure fields aren't empty
            tk.messagebox.showinfo('Missing Info', 'Please make sure both source and destination fields contain a correct file path.')
        else:
            source = source+"/"
            files = os.listdir(source)
            today = datetime.datetime.now()
            yesterday = today - timedelta(days=1)
            newFiles = []

            for i in files:
                modTime = datetime.datetime.fromtimestamp(os.path.getmtime(source+i))
                if modTime < yesterday: ##Check date modified of each file
                    continue
                else:
                    newFiles.append(i)##if the file is new, add it to the newfiles list

            if tk.messagebox.askyesno('Copy New Files?', str(len(newFiles))+' new files were found.\nWould you like to copy them?'):##get user confirmation to copy files
                for i in newFiles:
                    shutil.copy(source+i,destination) ##copy files and confirm to user
                tk.messagebox.showinfo('Files Copied', str(len(newFiles))+' new files were successfully copied.')

    def ask_quit(self):
        if tk.messagebox.askokcancel("Exit program", "Okay to exit application?"):
            # This closes app
            self.master.destroy()
            os._exit(0)        

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()


