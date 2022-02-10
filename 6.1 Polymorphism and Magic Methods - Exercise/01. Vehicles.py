from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, km):
        pass

    @abstractmethod
    def refuel(self, km):
        pass


class Car(Vehicle):
    AIR_CONDITION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, km):
        fuel_cost = km * (self.fuel_consumption + Car.AIR_CONDITION)
        if self.fuel_quantity >= fuel_cost:
            self.fuel_quantity -= fuel_cost

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITION = 1.6
    LOST_FUEL = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, km):
        fuel_cost = km * (self.fuel_consumption + Truck.AIR_CONDITION)
        if self.fuel_quantity >= fuel_cost:
            self.fuel_quantity -= fuel_cost

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * Truck.LOST_FUEL)


# --------------------------------------------------------


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
#
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

'''
2.299999999999997
12.299999999999997

17.0
64.5
'''


