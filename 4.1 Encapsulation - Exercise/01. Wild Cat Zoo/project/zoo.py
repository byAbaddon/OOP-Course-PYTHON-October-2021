class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return 'Not enough budget'
        if self.__animal_capacity == len(self.animals):
            return 'Not enough space for animal'
        self.animals.append(animal)
        self.__budget -= price
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker):
        if self.__workers_capacity > 0:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return f'Not enough space for worker'

    def fire_worker(self, worker_name):
        try:
            worker_to_fire = [x for x in self.workers if x.name == worker_name][0]
            self.workers.remove(worker_to_fire)
            return f'{worker_name} fired successfully'

        except:
            return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        all_salary = sum([x.salary for x in self.workers])
        if self.__budget >= all_salary:
            self.__budget -= all_salary
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        budget_needed = 0
        for animal in self.animals:
            budget_needed += animal.money_for_care
        if self.__budget >= budget_needed:
            self.__budget -= budget_needed
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'

        lions = [x.__repr__() for x in self.animals if x.__class__.__name__ == 'Lion']
        result += f'----- {len(lions)} Lions:\n'
        result += '\n'.join(lions) + '\n'

        tigers = [x.__repr__() for x in self.animals if x.__class__.__name__ == 'Tiger']
        result += f'----- {len(tigers)} Tigers:\n'
        result += '\n'.join(tigers) + '\n'

        cheetahs = [x.__repr__() for x in self.animals if x.__class__.__name__ == 'Cheetah']
        result += f'----- {len(cheetahs)} Cheetahs:\n'
        result += '\n'.join(cheetahs)
        return result

    def workers_status(self):
        result = f'You have {len(self.workers)} workers'

        keepers = [x.__repr__() for x in self.workers if x.__class__.__name__ == 'Keeper']
        result += f'\n----- {len(keepers)} Keepers:\n'
        result += '\n'.join(keepers)

        caretakers = [x.__repr__() for x in self.workers if x.__class__.__name__ == 'Caretaker']
        result += f'\n----- {len(caretakers)} Caretakers:\n'
        result += '\n'.join(caretakers)

        vets = [x.__repr__() for x in self.workers if x.__class__.__name__ == 'Vet']
        result += f'\n----- {len(vets)} Vets:\n'
        result += '\n'.join(vets)
        return result
