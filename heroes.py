import random
from abc import ABC, abstractmethod
import pytest


class Character(ABC):
    @abstractmethod
    def __init__(self):
        self.__hit_points = None
        self.__health_points = None

    @abstractmethod
    def set_hit_points(self):
        pass

    @abstractmethod
    def set_health_points(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Hero:
    heroes = ['Iron Man', 'Captain America']

    power_bonus = {
        'laser': 10,
        'punches and kick': 5,
        'strength': 8,
        'strategy': 3,

    }

    defense_bonus = {
        'armor': 5,
        "shield": 12,
        "speed": 5,
        "force": 24
    }

    @classmethod
    def get_hero(cls):
        return random.choice(Hero.heroes)

    @staticmethod
    def factory(hero_type, name):

        if hero_type == 'Iron Man':
            return IronMan(name)

        elif hero_type == 'Captain America':
            return CaptainAmerica(name)

        else:
            return None


class IronMan(Character, Hero):
    def __init__(self, name):
        Character.__init__(self)
        self.type = "Iron Man"
        self.__name = name
        self.__power = 'laser'

    def set_new_special_power(self, power):
        self.__power = power

    def set_hit_points(self):
        points = random.randint(5, 10)
        self.__hit_points = points

    def set_health_points(self):
        points = random.randint(45, 100)
        self.__health_points = points

    def get_info(self):
        print("########INFO########")
        print(f'Hero: {self.type}')
        print(f'Special power:{self.__power}')
        print(f'Hit points:{self.__hit_points}')
        print(f'Health points:{self.__health_points}')

    def get_power_bonus(self):
        power = self.power_bonus.get(self.__power)
        return power


class CaptainAmerica(Character, Hero):
    def __init__(self, name):
        Character.__init__(self)
        self.type = "CaptainAmerica"
        self.__name = name
        self.__power = 'shield'

    def set_new_special_power(self, power):
        self.__power = power

    def set_hit_points(self):
        points = random.randint(1, 10)
        self.__hit_points = points

    def set_health_points(self):
        points = random.randint(20, 100)
        self.__health_points = points

    def get_info(self):
        print("########INFO########")
        print(f'Hero: {self.type}')
        print(f'Special power:{self.__power}')
        print(f'Hit points:{self.__hit_points}')
        print(f'Health points:{self.__health_points}')

    def get_power_bonus(self):
        power = self.power_bonus.get(self.__power)
        return power


# obj instances


@pytest.mark.parametrize("class_objects", ["Bob", "Charley"])
def test_possbile_outputs(class_objects):
    hero = Hero.get_hero()
    hero_obj = Hero.factory(hero, class_objects)
    hero_obj.set_hit_points()
    hero_obj.set_health_points()
    hero_obj.get_info()


test_possbile_outputs("Charley")