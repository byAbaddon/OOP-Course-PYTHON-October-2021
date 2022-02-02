class Store:
    items = {}
    def __init__(self, name, type, capacity) :
        self.name = name
        self.type = type
        self.capacity = capacity

    @classmethod
    def from_size (cls, name, type, size):
        return Store(name, type, size // 2)

    def add_item(self, item_name):
        if self.capacity > 0:
            self.items[item_name] = 1
            return f'{item_name} added to the store'
        return 'Not enough capacity in the store'

    def remove_item(self, item_name, amount):
        if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name]=- amount
            return f'{amount} {item_name} removed from the store'   
        return f'Cannot remove {amount} {item_name}'

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'
