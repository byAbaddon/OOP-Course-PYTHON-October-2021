from abc import ABC, abstractmethod


class Card(ABC):
    @abstractmethod
    def __init__(self, name, damage_points, health_points):
        self.name = name
        self.damage_points = damage_points
        self.health_points = health_points

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if val == '':
            raise ValueError('Card\'s name cannot be an empty string.')
        self._name = val

    @property
    def damage_points(self):
        return self._damage_points

    @damage_points.setter
    def damage_points(self, val):
        if val < 0:
            raise ValueError('Card\'s damage points cannot be less than zero.')
        self._damage_points = val

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, val):
        if val < 0:
            raise ValueError('Card\'s HP cannot be less than zero.')
        self._health_points = val
