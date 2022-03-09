from tkinter import *

from tkinter import messagebox

import tkinter as tk



#Import other modules
import StudentTrackerGUI
import StudentTrackerFUNC

#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame configuration
        self.master = master
        self.master.minsize(500,350) #(Height, Width)
        self.master.maxsize(500,350)
        # This CenterWindow method will center our app on the user's screen
        StudentTrackerFUNC.center_window(self,500,350)
        self.master.title("Student Tracker App")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner "X" on Windows
        self.master.protocol("WM_DELETE_WINDOW", lambda: StudentTrackerFUNC.ask_quit(self))

        # load in the GUI widgets from a separate module,
        # keeping your code compartmentalized
        StudentTrackerGUI.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
