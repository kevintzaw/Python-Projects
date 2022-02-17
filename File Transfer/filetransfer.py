import shutil
import os

#importing time and tkinter
import time
import tkinter
from tkinter import *
import webbrowser

#setting an input screen
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.config(bg='lightgray')

        #creating variables for text with Source and Destination Folder
        self.varFolderSourcetext = StringVar()
        self.varFolderDestinationtext = StringVar()

        self.lblDisplay = Label(self.master, text='', font=("Helvetica",16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        #entry for Folder Source
        self.txtFolderSourcetext = Entry(self.master,text=self.varFolderSourcetext, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtFolderSourcetext.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        #entry for Destination Source
        self.txtFolderDestinationtext = Entry(self.master,text=self.varFolderDestinationtext, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtFolderDestinationtext.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        #submit button
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

 def submit(self):
        #set what the source folder is
        varSource = self.varFolderSourcetext.get()
        #set what the destination folder is
        varDestination = self.varDestinationSourcetext.get()
        files = os.listdir(varSource)

        for i in files:
            #we are saying move the files represented by 'i' to their new destination
            shutil.move(varSource+i, destination)

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

