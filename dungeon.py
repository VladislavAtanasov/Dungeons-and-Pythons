from Our_Hero import Hero
from spell import Spell
from weapon import Weapon
import random


class Dungeon:

    def __init__(self):
        map_file = open("map.txt")
        contents = map_file.read().strip("\n")
        self.result = contents.split(",")
        self.position = [[elem for elem in line] for line in self.result]
        self.hero = Hero("Gayster", "GaySlayer", 50, 20)
        self.treasures = {"mana": [10, 15, 20, 30],
                            "health": [10, 12, 17, 23],
                            "weapon": [Weapon("Axe", 20), Weapon("Water_sword", 40)],
                            "spell": [Spell("low_level", 10, 20, 1), Spell("strong", 30, 70, 6)]
                            }

    def __str__(self):
        return "S.##.....T\n#T##..###.\n#.###E###E\n#.E...###.\n###T#####G"

    def print_map(self):
        string = ""
        for elem in self.position:
            for e in elem:
                string += e
            string += '\n'
        return string

    def can_spawn(self):
        for c in self.position:
            for e in c:
                if e == "S":
                    return True
        else:
            return False

    def spawn(self, hero):
        if self.can_spawn():
            for elem in self.position:
                for e in elem:
                    if e == "S":
                        self.position[self.position.index(elem)][elem.index(e)] = "H"

    '''def swap(self):
        for c in self.position:
                for e in c:
                    self.position[self.position.index(c) - 1][c.index(e)] = "H"
                    self.position[self.position.index(c)][c.index(e)] = "."'''

    def move_hero(self, direction):
        if direction not in ["up", "down", "left", "right"]:
            raise ValueError("Invalid direction")
        if direction == "up":
            for elem in self.position:
                for e in elem:
                    if e == "H":
                        #needed_index = elem.index(e)
                        if self.position.index(elem) - 1 >= 0:
                            if self.position[self.position.index(elem) - 1][elem.index(e)] == ".":
                                self.position[self.position.index(elem) - 1][elem.index(e)] = "H"
                                self.position[self.position.index(elem)][elem.index(e)] = "."
                                if self.hero.mana + self.hero.mana_regeneration_rate <= 50:
                                    self.hero.mana += self.hero.mana_regeneration_rate
                                return True
                            elif self.position[self.position.index(elem) - 1][elem.index(e)] == "#":
                                return False
                            elif self.position[self.position.index(elem) - 1][elem.index(e)] == "T":
                                pass
                            elif self.position[self.position.index(elem) - 1][elem.index(e)] == "E":
                                pass
                        else:
                            return "Game over"

        elif direction == "down":
            for elem in self.position:
                for e in elem:
                    if e == "H":
                        #needed_index = elem.index(e)
                        if self.position.index(elem) + 1 <= len(self.position) - 1:
                            if self.position[self.position.index(elem) + 1][elem.index(e)] == ".":
                                self.position[self.position.index(elem) + 1][elem.index(e)] = "H"
                                self.position[self.position.index(elem)][elem.index(e)] = "."
                                if self.hero.mana + self.hero.mana_regeneration_rate <= 50:
                                    self.hero.mana += self.hero.mana_regeneration_rate
                                return True
                            elif self.position[self.position.index(elem) + 1][elem.index(e)] == "#":
                                return False
                            elif self.position[self.position.index(elem) + 1][elem.index(e)] == "T":
                                pass
                            elif self.position[self.position.index(elem) + 1][elem.index(e)] == "E":
                                pass
                        else:
                            return "Game over"

        elif direction == "right":
            for elem in self.position:
                for e in elem:
                    if e == "H":
                        #needed_index = elem.index(e)
                        if elem.index(e) + 1 <= len(elem) - 1:
                            if self.position[self.position.index(elem)][elem.index(e) + 1] == ".":
                                self.position[self.position.index(elem)][elem.index(e) + 1] = "H"
                                self.position[self.position.index(elem)][elem.index(e)] = "."
                                if self.hero.mana + self.hero.mana_regeneration_rate <= 50:
                                    self.hero.mana += self.hero.mana_regeneration_rate
                                return True
                            elif self.position[self.position.index(elem)][elem.index(e) + 1] == "#":
                                return False
                            elif self.position[self.position.index(elem)][elem.index(e) + 1] == "T":
                                random_treasure = random.choice(self.treasures.keys())
                                if random_treasure == "health":
                                    random_health = random.choice(self.treasures["health"])
                                    if self.hero.health + random_health <= 100:
                                        self.hero.health += random_health
                                elif random_treasure == "mana":
                                    random_mana = random.choice(self.treasures["mana"])
                                    if self.hero.mana + random_mana <= 50:
                                        self.hero.mana += random_mana
                                elif random_treasure == "weapon":
                                    random_weapon = random.choice(self.treasures["weapon"])
                                    self.hero.equip(self.random_weapon)
                                elif random_treasure == "spell":
                                    random_spell = random.choice(self.treasures["spell"])
                                    self.hero.learn(self.random_spell)
                                self.position[self.position.index(elem)][elem.index(e) + 1] = "H"
                                self.position[self.position.index(elem)][elem.index(e)] = "."
                                return True
                            elif self.position[self.position.index(elem)][elem.index(e) + 1] == "E":
                                pass
                        else:
                            return "Game over"

        elif direction == "left":
            for elem in self.position:
                for e in elem:
                    if e == "H":
                        #needed_index = elem.index(e)
                        if elem.index(e) - 1 >= 0:
                            if self.position[self.position.index(elem)][elem.index(e) - 1] == ".":
                                self.position[self.position.index(elem)][elem.index(e) - 1] = "H"
                                self.position[self.position.index(elem)][elem.index(e) + 1] = "."
                                if self.hero.mana + self.hero.mana_regeneration_rate <= 50:
                                    self.hero.mana += self.hero.mana_regeneration_rate
                                return True
                            elif self.position[self.position.index(elem)][elem.index(e) - 1] == "#":
                                return False
                            elif self.position[self.position.index(elem)][elem.index(e) - 1] == "T":
                                pass
                            elif self.position[self.position.index(elem)][elem.index(e) - 1] == "E":
                                pass

                        else:
                            return "Game over"





#hero = Hero("Gayster", "GaySlayer")
s = Dungeon()
print(s.print_map())
print(s.position)
s.spawn(s.hero)
print(s.print_map())
#print(s.move_hero("left"))
print(s.move_hero("right"))
print(s.print_map())
print(s.hero.mana)
print(s.hero.health)
