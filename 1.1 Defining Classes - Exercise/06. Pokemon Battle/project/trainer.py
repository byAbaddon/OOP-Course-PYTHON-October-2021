from pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon.name not in [x.name for x in self.pokemon]:
            self.pokemon.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'
        return 'This pokemon is already caught'

    def release_pokemon(self, pokemon_name):
        if pokemon_name not in [x.name for x in self.pokemon]:
            return f'Pokemon is not caught'
        pok_name = [x for x in self.pokemon if x.name == pokemon_name][0]
        self.pokemon.remove(pok_name)
        return f'You have released {pokemon_name}'

    def trainer_data(self):
        return f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n- {"".join([x.pokemon_details() for x in self.pokemon])}\n'

#
# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())