class Animal:
    sound = ""

    def __init__(self, name):
        self.name = name

    def set_category(self, sound):
        self.sound = sound


class Pig(Animal):
    sound = 'quizquiz'


class Cat(Animal):
    sound='meow meow'

class Dog(Animal):
    sound='bark bark'

class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.sound

    def print_animals_sounds(self):
        for animal in self.current_animals:
            print(f"{animal} is making the sound {self.current_animals[animal]}")


if __name__ == '__main__':
    zoo = Zoo()
    dog = Dog("Chuwuauwa")
    cat = Cat("Persian")
    pig = Pig ('Scrof')
    zoo.add_animal(dog)
    zoo.add_animal(cat)
    zoo.add_animal(pig)
    zoo.print_animals_sounds()
