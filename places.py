from abc import ABC, abstractmethod


class Place(ABC):
    @property
    def name(self):
        pass

    @abstractmethod
    def get_antagonist(self):
        pass


class Kostroma(Place):
    name = 'Kostroma'

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = 'Tokyo'

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')


class Planet(Place):
    name = 'Pandora ' + ';'.join(map(str, [123.45, 67.89]))

    def get_antagonist(self):
        print('Aliens are close')
