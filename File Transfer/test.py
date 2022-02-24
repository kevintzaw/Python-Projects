import shutil
import os

#importing time and tkinter
import time
import tkinter
from tkinter import *
import webbrowser
from tkinter import filedialog

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
        self.txtFolderDestinationtext.grid(row=2, column=1, padx=(30,0), pady=(30,0))

        #submit button
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=3, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        #button for choosing the source folder
        self.btnSource = Button(self.master, text="Choose Source", command=self.chooseSource)
        self.btnSource.grid(row=1, column=2, padx=(30,0), pady=(30,0))

        #button for choosing the destination folder
        self.btnDest = Button(self.master, text="Choose Destination", command=self.chooseDest)
        self.btnDest.grid(row=2, column=2, padx=(30,0), pady=(30,0))

    def chooseDest(self):
        #allows the user to choose the destinaton folder, and saves it to "dest"
        dest = filedialog.askdirectory()
        #inserts the path to the "dest" folder into the second Entry widget
        self.txtFolderDestinationtext.insert(0, dest)

    def chooseSource(self):
        #allows the user to choose the destinaton folder, and saves it to "Source"
        sourc = filedialog.askdirectory()
        #inserts the path to the "dest" folder into the second Entry widget
        self.txtFolderSourcetext.insert(0, sourc)

    def submit(self):
        #set what the source folder is
        varSource = self.varFolderSourcetext.get()
        #set what the destination folder is
        varDestination = self.varFolderDestinationtext.get()
        files = os.listdir(varSource)

        for i in files:
            #we are saying move the files represented by 'i' to their new destination
            print (i)
            print (varSource+"/"+i)

            variablePlusI = varSource+"/"+i

            #create variable for path and print how long it takes
            modification_time = os.path.getmtime(variablePlusI)
            print("Last modification tim since the epoch:", modification_time)

            #convert time in seconds since localtime
            localtime = time.ctime(modification_time)
            print("Last modification time(Local time):", localtime)

            if modification_time > 86400:
                if i != ".DS_Store":
                    shutil.move(variablePlusI, varDestination)

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

