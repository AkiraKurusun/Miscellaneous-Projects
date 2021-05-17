# Ethan Frailey
# TkinterTools
# 2/21

from tkinter import *

# Atributes
HEIGHT = 200 #INT
WIDTH = 200 #INT
FULLSCREEN = False #BOOLEAN


class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Creates The Widgets in the Program
        pass



def launch():
    root = Tk()
    root.title("Tkinter")
    root.geometry(str(str(WIDTH)+"x"+str(HEIGHT)))
    root.attributes("-fullscreen", FULLSCREEN)
    app = App(root)
    root.mainloop()

launch()