from tkinter import *

from tkinter import messagebox

import tkinter as tk



#Import other modules
import PhonebookGUI
import PhonebookFUNC

#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        PhonebookFUNC.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner "X" on Windows
        self.master.protocol("WM_DELETE_WINDOW", lambda: PhonebookFUNC.ask_quit(self))

        # load in the GUI widgets from a separate module,
        # keeping your code compartmentalized
        PhonebookGUI.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
