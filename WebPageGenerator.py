import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import messagebox


class ParentWindow(Frame):

    ##CREATE GUI
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(490,183))
        self.master.title('Create Custom Web Page')
        self.master.config(bg = 'lightgray')

        self.txtLabel = Label(self.master, text='Enter text for your web page...', bg='lightgray', width = 50)
        self.txtLabel.grid(row=0, column=0, columnspan = 2, padx=(20,0), pady=(40,0))

        self.txtEntry = Entry(self.master, text='', width = 73)
        self.txtEntry.grid(row=1, column=0, columnspan = 2, padx=(20,0), pady=(10,0))

        self.btnCreate = Button(self.master, text="Create Web Page", command=self.createWebPage, width=15, height=2)
        self.btnCreate.grid(row=2, column=0, padx=(0,10), pady=(10,0), sticky=E)

        self.btnClose = Button(self.master, text="Close Program", command=self.ask_quit, width=15, height=2)
        self.btnClose.grid(row=2, column=1, padx=(10,0), pady=(10,0), sticky=W)

    ##CREATE WEB PAGE
    def createWebPage(self):
        varHTML_Text = self.txtEntry.get() ##Get text from entry box.
        varHTML_Text = varHTML_Text.strip() ##Get rid of leading and trailing spaces.
        if (len(varHTML_Text) == 0): ##Show error if entry box is blank.
            messagebox.showerror("Missing Text", "Please enter text for your web page.")
        else: ##Create web page
            f = open("MyWebPage.html", "w")
            f.write("<html>\n\t<body>\n\t\t<h1>\n\t\t"+varHTML_Text+"\n\t\t</h1>\n\t</body>\n</html>")
            f.close()

            webbrowser.open("MyWebPage.html")

    ##CLOSE APPLICATION
    def ask_quit(self):
        if messagebox.askokcancel("Exit program", "Okay to exit application?"):
            # This closes app
            self.master.destroy()
            os._exit(0)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
