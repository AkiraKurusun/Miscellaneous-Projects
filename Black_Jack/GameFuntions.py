# Ethan Frailey
# 1/4/2021
# Game Functions

# Validates if a number is in a range
def get_float(prompt, min, max):
    while True:
        try:
            input_string = input(prompt)
            input_float = float(input_string)

            if (input_float >= min) and (input_float <= max):
                return input_float

        except:
            continue


class Validator:

    def get_integer(self, Min, Max):

        while True:
            try:
                input_string = input(self)
                input_int = int(input_string)

                if (input_int >= Min) and (input_int <= Max):
                    return input_int
            except:
                continue


# MENU FUNCTION
def menu_opt(options):
    """Pass through a list named options"""
    index = 1
    while True:
        for option in options:
            print(str.format("{}........{}", index, option))
            index += 1
        choose = input("Enter a number between 1 and " + str(len(options)) + " ")
        if choose.isnumeric():
            choose = int(choose)
            if 1 <= choose <= len(options):
                return choose
            else:
                print("Not an option")
        else:
            print("Not an option")


def ask_yes_or_no(question):
    """Ask yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


class Player(object):

    def __init__(self, name):
        self.name = name
        self.score = Score()
        self.lives = 3


class Score(object):

    def __init__(self):
        self.value = 0
        self.stepvalue = 10

    def add_score(self, itemid):
        for i in range(itemid):
            self.value += self.stepvalue

    def take_score(self, itemid):
        for i in range(itemid):
            self.value -= self.stepvalue
            if self.value < 0:
                self.value = 0


if __name__ == "__main__":
    print("You ran this module directly (and did not import it)")
    input("\n\nPress Enter to exit")
