from heroes import *
from places import *
from media import *


def save_the_place(hero: AttackHero, place: Place, media: Media):
    hero.find(place)
    hero.attack()
    if hero.ultimate_attack:
        hero.ultimate()
    media.create_news(hero, place)


if __name__ == '__main__':
    save_the_place(SuperMan('Clark Kent'), Kostroma(), Newspapers())
    print('-' * 50)
    save_the_place(SuperHero('Chuck Norris'), Tokyo(), Radio())
    print('-' * 50)
    save_the_place(Avatar('Jake Sully'), Planet(), TV())
