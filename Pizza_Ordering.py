# Ethan Frailey
# 1/21
# Pizza Ordering Guide

from tkinter import *


class App(Frame):
    """This is a GUI that counts login clicks"""

    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack()
        self.toppings = ["Cheese", "Mushrooms", "Pineapple", "Ham", "Steak", "Sausages", "Peppers", "Bacon",
                         "Buffalo Meat", "Chicken", "Extra Cheese", "Olives"]
        self.check_varibles = []

        self.Cheese_var = BooleanVar()
        self.check_varibles.append(self.Cheese_var)

        self.Mushrooms_var = BooleanVar()
        self.check_varibles.append(self.Mushrooms_var)

        self.Pineapple_var = BooleanVar()
        self.check_varibles.append(self.Pineapple_var)

        self.Ham_var = BooleanVar()
        self.check_varibles.append(self.Ham_var)

        self.Steak_var = BooleanVar()
        self.check_varibles.append(self.Steak_var)

        self.Sausages_var = BooleanVar()
        self.check_varibles.append(self.Sausages_var)

        self.Peppers_var = BooleanVar()
        self.check_varibles.append(self.Peppers_var)

        self.Bacon_var = BooleanVar()
        self.check_varibles.append(self.Bacon_var)

        self.Buffalo_Meat_var = BooleanVar()
        self.check_varibles.append(self.Buffalo_Meat_var)

        self.Chicken_var = BooleanVar()
        self.check_varibles.append(self.Chicken_var)

        self.Extra_Cheese_var = BooleanVar()
        self.check_varibles.append(self.Extra_Cheese_var)

        self.Olives_var = BooleanVar()
        self.check_varibles.append(self.Olives_var)

        self.create_widgets()

    def create_widgets(self):
        # Create all Widgets

        title_label = Label(self, text="Welcome To PizzaPlanet")

        label_split = Label(self, text="-----------------------------------------")
        label_split1 = Label(self, text="-----------------------------------------")
        label_split2 = Label(self, text="-----------------------------------------")
        label_split3 = Label(self, text="-----------------------------------------")
        label_split4 = Label(self, text="-----------------------------------------")

        information_label = Label(self, text="Enter the following information:")
        name_label = Label(self, text="Name:")
        number_label = Label(self, text="Phone Number:")
        address_label = Label(self, text="Address:")
        size_label = Label(self, text="Select Your Size:")
        crust_label = Label(self, text="Select Your Crust:")
        toppings_label = Label(self, text="Select Your Toppings:")
        submit_button = Button(self, text="Place Your Order", command=self.submit)
        self.submission_text_box = Text(self, width=25, height=10)
        self.submission_text_box.config(state=DISABLED)

        self.name_input = Entry(self)
        self.number_input = Entry(self)
        self.address_input = Entry(self)


        self.size = StringVar()
        self.size.set("Extra Large")
        Large = Radiobutton(self, text="Large", value="Large", variable=self.size)
        Medium = Radiobutton(self, text="Medium", value="Medium", variable=self.size)
        Small = Radiobutton(self, text="Small", value="Small", variable=self.size)
        E_Large = Radiobutton(self, text="Extra Large", value="Extra Large", variable=self.size)


        self.crust = StringVar()
        self.crust.set("Stuffed")
        stuffed_crust = Radiobutton(self, text="Stuffed", value="Stuffed", variable=self.crust)
        deep_dish = Radiobutton(self, text="Deep Dish", value="Deep Dish", variable=self.crust)
        garlic_crust = Radiobutton(self, text="Garlic Crust", value="Garlic Crust", variable=self.crust)
        Neapolitan = Radiobutton(self, text="Neapolitan", value="Neapolitan", variable=self.crust)
        New_Haven_Style = Radiobutton(self, text="New Haven Style", value="New Haven Style", variable=self.crust)
        Flatbread = Radiobutton(self, text="Flatbread", value="Flatbread", variable=self.crust)

        title_label.grid(row=1, columnspan=2, sticky=N)
        label_split.grid(row=2, columnspan=2)
        information_label.grid(row=3, columnspan=2, sticky=N)

        name_label.grid(row=4, column=0, sticky=W)
        self.name_input.grid(row=4, column=1, sticky=N)
        number_label.grid(row=5, column=0, sticky=W)
        self.number_input.grid(row=5, column=1, sticky=W)
        address_label.grid(row=6, column=0, sticky=W)
        self.address_input.grid(row=6, column=1, sticky=W)
        label_split1.grid(row=7, columnspan=2)

        size_label.grid(row=8, column=0, sticky=W)
        Large.grid(row=9, column=0, sticky=W)
        Medium.grid(row=9, column=1, sticky=W)
        Small.grid(row=10, column=0, sticky=W)
        E_Large.grid(row=10, column=1, sticky=W)
        label_split2.grid(row=11, columnspan=2)

        crust_label.grid(row=12, sticky=W)
        stuffed_crust.grid(row=13, column=0, sticky=W)
        deep_dish.grid(row=13, column=1, sticky=W)
        garlic_crust.grid(row=14, column=0, sticky=W)
        Neapolitan.grid(row=14, column=1, sticky=W)
        New_Haven_Style.grid(row=15, column=0, sticky=W)
        Flatbread.grid(row=15, column=1, sticky=W)
        label_split3.grid(row=16, columnspan=2)

        toppings_label.grid(row=17, sticky=W)

        for i in range(len(self.toppings)):
            row = 18 + i // 2
            column = i % 2
            checkbox = Checkbutton(self,
            text=self.toppings[i],
            variable=self.check_varibles[i],
            command=self.update).grid(row=row, column=column, sticky=W)

        label_split4.grid(row=24, columnspan=2)
        submit_button.grid(row=25, columnspan=2)
        self.submission_text_box.grid(row=26, columnspan=2, padx=10, pady=8)

    def submit(self):
        text = ""
        text += "Name: " + self.name_input.get() + "\n"
        text += "Number: " + self.number_input.get() + "\n"
        text += "Address: " + self.address_input.get() + "\n"
        text += "----------------" + "\n"
        text += "Size: " + self.size.get() + "\n"
        text += "Crust: " + self.crust.get() + "\n"
        text += "Toppings: " + "\n"
        for i in range(len(self.check_varibles)):
            if self.check_varibles[i].get():
                text += "- " + self.toppings[i] + "\n"

        self.submission_text_box.delete(0.0, END)
        self.submission_text_box.insert(0.0, text)





def main():
    root = Tk()
    root.title("PizzaPlanet")
    # root.geometry("250x500")
    root.attributes("-fullscreen", False)
    root.resizable(0,0)
    root.config(bg="lightgray")
    app = App(root)
    root.mainloop()


main()
