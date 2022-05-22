class Animal:

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("silence...")


class Dog:

    def __init__(self):
        self.animal = Animal("Dog")

    def make_sound(self):
        print(f"{self.animal.name} is barking !")


class Pig:

    def __init__(self):
        self.animal = Animal("Pig")

    def make_sound(self):
        print(f"{self.animal.name} is quitzquitz")


class Cat:

    def __init__(self):
        self.animal = Animal("Cat")

    def make_sound(self):
        print(f"{self.animal.name} is Meowing!")


if __name__ == '__main__':

    animals = list()

    animals.append(Dog())
    animals.append(Pig())
    animals.append(Cat())

    for animal in animals:
        animal.make_sound()

