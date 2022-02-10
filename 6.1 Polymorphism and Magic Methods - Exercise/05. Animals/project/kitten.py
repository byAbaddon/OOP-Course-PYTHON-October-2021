# from cat import Cat
from project.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender='Female')

    def __repr__(self):
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}'

    def make_sound(self):
        return 'Meow'


# kitten = Kitten("Kiki", 1)
# print(kitten.make_sound())
# print(kitten)