class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('The name cannot be an empty string')
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError('You should add dough to the pizza')
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError('The topping\'s capacity cannot be less or equal to zero')
        self.__toppings_capacity = value

    def add_topping(self, topping):
        type_pizza = topping.topping_type
        weight = topping.weight
        if self.toppings_capacity <= len(self.toppings):
            raise ValueError('Not enough space for another topping')
        if type_pizza not in self.toppings:
            self.toppings[type_pizza] = 0
        self.toppings[type_pizza] += weight

    def calculate_total_weight(self):
        return self.dough.weight + sum([self.toppings[x] for x in self.toppings])


