# Ethan Frailey
# TkinterTools
# 2/21

from tkinter import *
from tkinter import messagebox as mb

# Attributes
HEIGHT = 200 #INT
WIDTH = 200 #INT
FULLSCREEN = False #BOOLEAN


class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(fill=BOTH)
        self.create_widgets()

    def create_widgets(self):
        # Creates The Widgets in the Program
        error_button = Button(self, text="Error", command=self.onError)
        warning_button = Button(self, text="Warning", command=self.onWarning)
        question_button = Button(self, text="Question", command=self.onQuestion)
        info_button = Button(self, text="Info", command=self.onInfo)

        error_button.grid(row=0, column=0)
        warning_button.grid(row=0, column=1)
        question_button.grid(row=1, column=0)
        info_button.grid(row=1, column=1)

    def onError(self):
        mb.showerror("Error","Could Not Open File")

    def onWarning(self):
        mb.showwarning("Warning", "This is a Warning")

    def onQuestion(self):
        result = mb.askquestion("Question", "Are your sure you want to quit?")
        if result == "yes":
            sys.exit()
        else:
            pass


    def onInfo(self):
        mb.showinfo("info", "Download Complete")


def launch():
    root = Tk()
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    root.attributes("-fullscreen", FULLSCREEN)
    root.title("Dialogue Boxes")
    app = App(root)
    root.mainloop()

launch()