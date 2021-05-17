# Ethan Frailey
# pet_project

import random


class Critter(object):
    """this is the class that defines what a critter is"""

    def __init__(self):
        self.health = 100
        self.hunger = 0
        self.height = 0
        self.weight = random.randint(2, 7)
        self.name = ""
        self.happiness = 100
        self.is_alive = True

    def die(self):
        print("You killed your pet. You monster!!")
        self.is_alive = False

    def set_name(self, name):
        if len(name) > 4:
            self.name = name

    def set_height(self, height):
        if 5 > int(height) > 1:
            self.height = height

    def intro(self):
        print("Hello, my name is " + self.get_name())

    def feed(self, food):
        if food == "pizza":
            self.hunger -= 7
        elif food == "cheese burger":
            self.hunger -= 13
        elif food == "steak":
            self.hunger -= 23
        elif food == "corn":
            self.hunger -= 3
        elif food == "cheesecake":
            self.hunger -= 100
        else:
            self.hunger -= 5

    def pass_time(self, hours):
        for i in range(hours):
            self.hunger += 2
            if self.hunger < 0:
                self.weight += 1
                self.happiness += 10
                self.health -= 5
            if self.hunger > 50:
                self.weight -= 1
                self.happiness -= 5
                self.health -= 5
            self.happiness -= 5

    def play(self, time):
        self.pass_time(self, time)
        self.happiness += 10 * time
        if self.happiness > 100:
            self.happiness = 100
        if self.health > 100:
            self.health = 100

    def get_health(self):
        return self.health

    def get_hunger(self):
        return self.hunger

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_happiness(self):
        return self.happiness

    def get_name(self):
        return self.name

    def hud(self):
        print(self.get_name())
        health = self.get_health()
        if health == 100:
            print("Perfect Health " + str(health))
        elif 100 > health <= 80:
            print("Good Health " + str(health))
        elif 80 > health <= 50:
            print("Average Health " + str(health))
        elif 50 > health <= 30:
            print("Poor Health " + str(health))
        elif 30 > health:
            print("Very Poor Health " + str(health))
        else:
            self.die()

        hunger = self.get_hunger()
        if 0 > hunger <= 30:
            print("Good " + str(hunger))
        elif 30 > hunger <= 50:
            print("Hungry " + str(hunger))
        elif 50 > hunger:
            print("Very hungry " + str(hunger))
        if 100 <= hunger:
            self.die()
        else:
            print("Hungry " + str(hunger))

        happy = self.get_happiness()
        if happy == 100:
            print("Very Happy " + str(happy))
        elif 100 > happy <= 80:
            print("Happy " + str(happy))
        elif 80 > happy <= 50:
            print("Neutral " + str(happy))
        elif 50 > happy <= 30:
            print("Not Happy " + str(happy))
        elif 30 > happy <= 10:
            print("Depressed " + str(happy))
        else:
            self.die()


def main():
    pet = Critter()
    name = input("What would you like your pet to be called ")
    pet.set_name(name)
    height = input("What is the height of you pet. Between 2 and 5 ")
    pet.set_height(height)
    pet.intro()
    pet.hud()
    while pet.is_alive:
        pet.pass_time(1)
        print("What do you want to do?")
        print("Feed")
        print("Play")
        print("Nothing")
        response = input()
        if response == "feed":
            food = input("What do you want to feed them")
            pet.feed(food)
        if response == "play":
            time = int(input("How long will you play with your pet "))
            pet.play(time)
        pet.hud()


main()
