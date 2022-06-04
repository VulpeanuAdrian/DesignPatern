from animal_types import Dog, Cat, Pig


class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.__class__.__name__] = animal.sound

    def print_animals_sounds(self):
        for animal in self.current_animals:
            print(f"{animal} is making the sound {self.current_animals[animal]}")


if __name__ == '__main__':
    zoo = Zoo()
    dog, cat, pig = Dog(), Cat(), Pig()
    zoo.add_animal(dog)
    zoo.add_animal(cat)
    zoo.add_animal(pig)
    zoo.print_animals_sounds()
