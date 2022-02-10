from abc import ABC


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def repr(self):
        pass

    def make_sound(self):
        pass

