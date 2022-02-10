# from animal import Animal
from project.animal import Animal


class Cat(Animal):
    def __repr__(self):
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}'

    def make_sound(self):
        return 'Meow meow!'


# cat = Cat("Johnny", 7, "Male")
# print(cat.make_sound())
# print(cat)