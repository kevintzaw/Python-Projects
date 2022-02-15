import tkinter
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray')

        self.varBodytext = StringVar()

        self.lblDisplay = Label(self.master, text='', font=("Helvetica",16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        self.txtBodytext = Entry(self.master,text=self.varBodytext, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtBodytext.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        

    def submit(self):
        bodytext = self.varBodytext.get()
        self.lblDisplay.config(text='Your text is {}!'.format(bodytext))
        finaltext = "<html> <body> {} </body> </html>".format(bodytext)
        print(finaltext)
        #creates HTML file
        f = open("demofile2.html", "w")
        
        #outputs text
        f.write(finaltext)
        f.close()

        filename = 'demofile2.html'
        webbrowser.open_new_tab(filename)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

