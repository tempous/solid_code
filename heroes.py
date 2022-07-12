from abc import ABC, abstractmethod
from attacks import *


class AttackHero(ABC):

    def __init__(self, name, ultimate_attack = False):
        self.name = name
        self.ultimate_attack = ultimate_attack

    def find(self, place):
        return place.get_antagonist()

    @abstractmethod
    def attack(self):
        pass


class UltimateHero(AttackHero):

    def __init__(self, name):
        super().__init__(name, ultimate_attack=True)

    @abstractmethod
    def ultimate(self):
        pass


class SuperMan(UltimateHero, Kick, Laser):

    def attack(self):
        self.roundhouse_kick()

    def ultimate(self):
        self.incinerate_with_lasers()


class SuperHero(AttackHero, Gun):

    def attack(self):
        self.fire_a_gun()


class Avatar(AttackHero, Laser):

    def attack(self):
        self.incinerate_with_lasers()
