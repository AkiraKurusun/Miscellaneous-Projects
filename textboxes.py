# demonstrates text and entry widgets, and the Grid layout manager

from tkinter import *


class App(Frame):

    usernames = ["EthanFrailey"]
    passwords = ["Password"]
    trys = 0

    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.title = Label(self, text="User Login")
        self.title.grid(row=0, column=0)

        self.user = Label(self, text="Username")
        self.user.grid(row=1, column=0)

        self.user_input = Entry(self)
        self.user_input.grid(row=1, column=1)

        self.passwrd = Label(self, text="Password")
        self.passwrd.grid(row=2, column=0)

        self.passwrd_input = Entry(self)
        self.passwrd_input.grid(row=2, column=1)

        self.login = Button(self, text="Log In")
        self.login.grid(row=3)
        self.login["command"]=self.submit

        self.new_user_button = Button(self, text = "Create New User")
        self.new_user_button.grid(row = 4)
        self.new_user_button["command"]=self.add_user()

        self.txtbox2 = Text(self, height=10, width=50)
        self.txtbox2.grid(row=4, columnspan=3, sticky = NE)

    def submit(self):
        username = self.user_input.get()
        password = self.passwrd_input.get()

        if username in self.usernames:
            if password in self.passwords:
                message = "You Got in"

            else:
                message = "Wrong Password"
                self.trys += 1

        else:
            message = "Non existent username"
            self.trys += 1

        if self.trys > 3:
            message = "contacting the authorites"

        self.txtbox2.delete(0.0,END)
        self.txtbox2.insert(0.0,message)

    def add_user(self):
        pass


def main():
    root = Tk()
    root.title("password entry")
    root.geometry("500x500")
    root.attributes("-fullscreen", False)
    app = App(root)
    root.mainloop()


main()
