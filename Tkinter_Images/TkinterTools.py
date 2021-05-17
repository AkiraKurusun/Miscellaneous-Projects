# Ethan Frailey
# TkinterTools
# 2/21

from tkinter import *
from PIL import Image, ImageTk

# Attributes
HEIGHT = 750 #INT
WIDTH = 250 #INT
FULLSCREEN = False #BOOLEAN



class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.index = 0
        self.index1 = 1
        self.index2 = 2
        self.pack(fill=BOTH, expand=1)
        self.create_widgets()

    def create_widgets(self):
        # Creates The Widgets in the Program
        self.config(bg="DarkGrey")
        Label(text="My Favorite Images").place(x=(WIDTH/2)-55,y=5)
        # Loading Images
        img1 = Image.open("Logo.png")
        img2 = Image.open("Title screen.jpg")
        img3 = Image.open("Arsene.jpg")
        # Converting them so they can be used
        self.logo1 = ImageTk.PhotoImage(img1)
        self.logo2 = ImageTk.PhotoImage(img2)
        self.logo3 = ImageTk.PhotoImage(img3)
        self.imglist = [self.logo1, self.logo2, self.logo3]

        self.imglbl1 = Label(self, image=self.imglist[0])
        self.imglbl1.image = self.imglist[0]
        self.imglbl1.place(x=25, y=75)

        self.imglbl2 = Label(self, image=self.imglist[1])
        self.imglbl2.image = self.imglist[1]
        self.imglbl2.place(x=25, y=260)

        self.imglbl3 = Label(self, image=self.imglist[2])
        self.imglbl3.image = self.imglist[2]
        self.imglbl3.place(x=25, y=375)

        change = Button(text="change img", command=self.changeimg)
        change.place(x=25, y = 600)

    def changeimg(self):
        self.index = ((self.index + 1) % 3)

        self.imglbl1.config(image=self.imglist[self.index])
        self.imglbl2.config(image=self.imglist[(self.index + 1) % 3])
        self.imglbl3.config(image=self.imglist[(self.index + 2) % 3])







def launch():
    root = Tk()
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    root.attributes("-fullscreen", FULLSCREEN)
    app = App(root)
    root.mainloop()

launch()