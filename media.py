from abc import ABC, abstractmethod

from heroes import AttackHero


class Media(ABC):
    @abstractmethod
    def create_news(self, hero, place):
        return f'{hero.name} saved the {place.name}!'


class Newspapers(Media):
    def create_news(self, hero, place):
        print(f'Newspapers: {super().create_news(hero, place)}')


class Radio(Media):
    def create_news(self, hero, place):
        print(f'Radio: {super().create_news(hero, place)}')


class TV(Media):
    def create_news(self, hero, place):
        print(f'TV: {super().create_news(hero, place)}')