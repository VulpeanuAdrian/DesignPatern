class Dog:
    def make_sound(self):
        return f"{self.__class__.__name__} is barking !"


class Pig:

    def make_sound(self):
        return f"{self.__class__.__name__} is quizquiz !"


class Cat:
    def make_sound(self):
        return f"{self.__class__.__name__} is meow !"


class Animal:

    def __init__(self):
        self.animal_list = [Dog(), Cat(), Pig()]

    def get_animal_sounds(self):
        for animal in self.animal_list:
            print(animal.make_sound())


if __name__ == '__main__':
    animals = Animal()
    animals.get_animal_sounds()
