from Our_Hero import Our_Hero, Spell, Weapon
from Enemies import Enemy
from random import *
import sys
from fight import Fight
from dungeon import Dungeon

def main():
    my_dungeon = Dungeon("area.txt")
    my_dungeon.spawn(my_dungeon.hero)
    my_dungeon.hero.learn(Spell("strong", 30, 70, 6))
    while my_dungeon.hero.is_alive():
        print(my_dungeon.print_map())
        command = input("Enter Direction: ")
        my_dungeon.move_hero(command)

if __name__ == '__main__':
    main()
