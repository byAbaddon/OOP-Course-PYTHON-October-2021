import os
os.system('clear')
class Animal:
   
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


def animal_sound(animals: list):
    animal_dict = {'cat' : 'meow' , 'dog' : 'woof-woof', 'chicken' : 'kut-kut'}
    for animal in animals:
        print(animal_dict[animal.species])
        


animals = [Animal('cat'), Animal('dog')]
animal_sound(animals)

animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
animal_sound(animals)