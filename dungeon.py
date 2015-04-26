from Our_Hero import Our_Hero, Spell, Weapon
from Enemies import Enemy
from random import *
import sys
from fight import Fight

class Dungeon(Fight):

    @staticmethod
    def load(file_name):
        opened = open(file_name, "r")
        my_file = opened.read().split("\n")
        lists = [lis for lis in my_file if lis.strip() != ""]
        place = [[elem for elem in x] for x in lists]
        opened.close()
        return place

    def __init__(self, file_name):
        self.place = Dungeon.load(file_name)
        self.treasures_list = {
                                "mana":[10,15,20,30],
                                "health":[10,12,17,23],
                                "weapon":[Weapon("Axe", 20), Weapon("Water_sword", 40)],
                                "spell":[Spell("low_level", 10, 20, 1), Spell("strong", 30, 70, 6)]}
        self.hero = Our_Hero("Gayster", "GaySlayer")
        self.enemy = Enemy(health=100, mana=100, damage=20)
        self.f = Fight(self.hero, self.enemy)
    def spawn(self, hero):
        if hero.is_alive():
            for elem in self.place:
                for x in elem:
                    if x == "S":
                        self.place[self.place.index(elem)][elem.index(x)] = "H"
                        return True
            else:
                return False
        else:
            return False

    def move_hero(self, direction):
        if direction not in ["up", "down", "left", "right"]:
            raise ValueError("Invalid direction")
        elif self.hero.is_alive():
            if direction == "up":
                for elem in self.place:
                    for x in elem:
                        if "H" in elem:
                            if self.place.index(elem) - 1 >= 0:
                                if self.place[self.place.index(elem) - 1][elem.index("H")] == ".":
                                    self.place[self.place.index(elem) - 1][elem.index("H")] = "H"
                                    self.place[self.place.index(elem)][elem.index("H")] = "."
                                    return True
                                if self.place[self.place.index(elem) - 1][elem.index("H")] == "#":
                                    return False
                                if self.place[self.place.index(elem) - 1][elem.index("H")] == "E":
                                    self.place[self.place.index(elem) - 1][elem.index("H")] = "H"
                                    self.place[self.place.index(elem)][elem.index("H")] = "."
                                    return self.f.start_attack()
                                if self.place[self.place.index(elem) - 1][elem.index("H")] == "T":
                                    self.place[self.place.index(elem) - 1][elem.index("H")] = "H"
                                    self.place[self.place.index(elem)][elem.index("H")] = "."
                                    return self.pick_treasure()
                                if self.place[self.place.index(elem) - 1][elem.index("H")] == "G":
                                    self.place[self.place.index(elem) - 1][elem.index("H")] = "H"
                                    self.place[self.place.index(elem)][elem.index("H")] = "."
                                    print("Our Hero Escaped! You win!")
                                    return sys.exit()
                            else:
                                return False
            if direction == "down":
                for elem in self.place:
                    for x in elem:
                        if "H" in elem:
                            if self.place.index(elem) + 1 <= len(self.place) - 1:
                                if self.place[self.place.index(elem) + 1][elem.index("H")] == ".":
                                    self.place[self.place.index(elem) + 1][elem.index("H")] = "H"
                                    self.place[self.place.index(elem)][elem.index("H")] = "."
                                    return True
                                if self.place[self.place.index(elem) + 1][elem.index("H")] == "#":
                                    return False
                                if self.place[self.place.index(elem) + 1][elem.index("H")] == "E":
                                    self.place[self.place.index(elem) + 1][elem.index("H")] = "H"
                                    self.place[self.place.index(elem)][elem.index("H")] = "."
                                    return self.f.start_attack()
                                if self.place[self.place.index(elem) + 1][elem.index("H")] == "T":
                                    self.place[self.place.index(elem) + 1][elem.index("H")] = "H"
                                    self.place[self.place.index(elem)][elem.index("H")] = "."
                                    return self.pick_treasure()
                                if self.place[self.place.index(elem) + 1][elem.index("H")] == "G":
                                    self.place[self.place.index(elem) + 1][elem.index("H")] = "H"
                                    self.place[self.place.index(elem)][elem.index("H")] = "."
                                    print("Our Hero Escaped! You win!")
                                    return sys.exit()
                            else:
                                return False
            if direction == "right":
                for elem in self.place:
                    for x in elem:
                        if "H" in elem:
                            if elem.index("H") + 1 <= len(elem) - 1:
                                if self.place[self.place.index(elem)][elem.index("H") + 1] == ".":
                                    self.place[self.place.index(elem)][elem.index("H") + 1] = "H"
                                    self.place[self.place.index(elem)][elem.index("H")] = "."
                                    return True
                                if self.place[self.place.index(elem)][elem.index("H") + 1] == "#":
                                    return False
                                if self.place[self.place.index(elem)][elem.index("H") + 1] == "E":
                                    self.place[self.place.index(elem)][elem.index("H") + 1] = "H"
                                    self.place[self.place.index(elem)][elem.index("H")] = "."
                                    return self.f.start_attack()
                                if self.place[self.place.index(elem)][elem.index("H") + 1] == "T":
                                    self.place[self.place.index(elem)][elem.index("H") + 1] = "H"
                                    self.place[self.place.index(elem)][elem.index("H")] = "."
                                    return self.pick_treasure()
                                if self.place[self.place.index(elem)][elem.index("H") + 1] == "G":
                                    self.place[self.place.index(elem)][elem.index("H") + 1] = "H"
                                    self.place[self.place.index(elem)][elem.index("H")] = "."
                                    print("Our Hero Escaped! You win!")
                                    return sys.exit()
                            else:
                                return False
            if direction == "left":
                for elem in self.place:
                    for x in elem:
                        if "H" in elem:
                            if elem.index("H") - 1 >= 0:
                                if self.place[self.place.index(elem)][elem.index("H") - 1] == ".":
                                    self.place[self.place.index(elem)][elem.index("H") - 1] = "H"
                                    self.place[self.place.index(elem)][elem.index("H") + 1] = "."
                                    return True
                                if self.place[self.place.index(elem)][elem.index("H") - 1] == "#":
                                    return False
                                if self.place[self.place.index(elem)][elem.index("H") - 1] == "E":
                                    self.place[self.place.index(elem)][elem.index("H") - 1] = "H"
                                    self.place[self.place.index(elem)][elem.index("H") + 1] = "."
                                    return self.f.start_attack()
                                if self.place[self.place.index(elem)][elem.index("H") - 1] == "T":
                                    self.place[self.place.index(elem)][elem.index("H") - 1] = "H"
                                    self.place[self.place.index(elem)][elem.index("H") + 1] = "."
                                    return self.pick_treasure()
                                if self.place[self.place.index(elem)][elem.index("H") - 1] == "G":
                                    self.place[self.place.index(elem)][elem.index("H") - 1] = "H"
                                    self.place[self.place.index(elem)][elem.index("H") + 1] = "."
                                    print("Our Hero Escaped! You win!")
                                    return sys.exit()
                            else:
                                return False
        else:
            print("Game Over")
            return True

    def pick_treasure(self):
        treasures = open("treasures.txt", "r")
        read = treasures.read().split("\n")
        list_treasures = [lis for lis in read if lis != ""]
        treasures.close()
        random_treasure = choice(range(0,len(list_treasures)))
        if list_treasures[random_treasure] == "Health Potion":
            random_health = choice(self.treasures_list["health"])
            self.hero.take_healing(random_health)
        elif list_treasures[random_treasure] == "Mana":
            random_mana = choice(self.treasures_list["mana"])
            self.hero.take_mana(random_mana)
        elif list_treasures[random_treasure] == "Weapon":
            random_weapon = choice(self.treasures_list["weapon"])
            self.hero.equip(random_weapon)
        elif list_treasures[random_treasure] == "Spell":
            random_spell = choice(self.treasures_list["spell"])
            self.hero.learn(random_spell)
        print("Found Treasure: {}".format(list_treasures[random_treasure]))

    def count_enemies(self):
        enemies_number = 0
        for position in self.place:
            for element in position:
                if element == "E":
                    enemies_number+= 1
        return enemies_number

    def hero_attack(self, by = ""):
        if by == "weapon":
            return self.hero.weapon != None
        elif by == "spell":
            return self.hero.spell != None

    def print_map(self):
        string = ""
        for pos in self.place:
            for elem in pos:
                string += elem
            string += '\n'
        return string

def main():
    m = Dungeon("area.txt")
    m.spawn(m.hero)
    m.hero.learn(Spell("strong", 30, 70, 6))
    #print(m.move_hero("right"))
    #print(m.move_hero("down"))
    #print(m.move_hero("down"))
    #print(m.move_hero("down"))
    #print(m.hero_attack(by="weapon"))
    #print(m.hero.mana)
    #print(m.move_hero("right"))
    #print(m.move_hero("right"))
    #print(m.print_map())

if __name__ == '__main__':
    main()
