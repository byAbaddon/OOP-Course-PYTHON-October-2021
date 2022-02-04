class Account:
    def __init__(self, id, balance, pin):
        self.balance = balance
        self.__id = id
        self.__pin = pin

    def get_id(self, pin):
        return self.__id if self.__pin == pin else "Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if self.__pin == old_pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"


# ----------------------------------------test
account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
'''
Wrong pin
8827312
100
Wrong pin
Pin changed
'''