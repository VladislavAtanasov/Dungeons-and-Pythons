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
                            "weapon": [Weapon("Axe", 20), Weapon("Water sword", 40)],
                            "spell": [Spell("low_level", 10, 20, 1), Spell("strong", 30, 70, 6)]
                            }
        self.random_treasure = None
        self.random_spell = None
        self.random_health = None
        self.random_mana = None

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

    def take_mana_when_moving(self):
        if self.hero.mana + self.hero.mana_regeneration_rate <= 50:
            #self.hero.mana += self.hero.mana_regeneration_rate
            self.hero.take_mana(self.hero.mana_regeneration_rate)

    def pick_treasure(self):
        random_treasure = random.choice(self.treasures.keys())
        if random_treasure == "health":
            self.random_health = random.choice(self.treasures["health"])
            if self.hero.health + self.random_health <= 100:
                self.hero.health += self.random_health
                return "Found health potion. Hero health increased by {}.".format(str(self.random_health))
            else:
                return "Found health potion. Hero health is max."
        elif random_treasure == "mana":
            self.random_mana = random.choice(self.treasures["mana"])
            if self.hero.mana + self.random_mana <= 50:
                self.hero.mana += self.random_mana
                return "Found mana poton. Hero mana increased by {}.".format(str(self.random_mana))
            else:
                return "Found mana potion. Hero mana is max."
        elif random_treasure == "weapon":
            self.random_weapon = random.choice(self.treasures["weapon"])
            self.hero.equip(self.random_weapon)
            return "Found weapon. Hero equipped with {}. Weapon damage is {}".format(self.hero.weapon.name, self.hero.weapon.damage)
        elif random_treasure == "spell":
            self.random_spell = random.choice(self.treasures["spell"])
            self.hero.learn(self.random_spell)
            return "Found spell. Hero learnt spell named {}. Spell damage is {}".format(self.hero.spell.name, self.hero.spell.damage)

    def move_hero(self, direction):
        if direction not in ["up", "down", "left", "right"]:
            raise ValueError("Invalid direction")

        if direction == "up":
            for elem in self.position:
                for e in elem:
                    if e == "H":
                        if self.position.index(elem) - 1 >= 0:
                            if self.position[self.position.index(elem) - 1][elem.index(e)] == ".":
                                self.position[self.position.index(elem) - 1][elem.index(e)] = "H"
                                self.position[self.position.index(elem)][elem.index(e)] = "."
                                self.take_mana_when_moving()
                                return True
                            elif self.position[self.position.index(elem) - 1][elem.index(e)] == "#":
                                return False
                            elif self.position[self.position.index(elem) - 1][elem.index(e)] == "T":
                                self.position[self.position.index(elem) - 1][elem.index(e)] = "H"
                                self.position[self.position.index(elem)][elem.index(e)] = "."
                                self.take_mana_when_moving()
                                return self.pick_treasure()
                            elif self.position[self.position.index(elem) - 1][elem.index(e)] == "E":
                                return "Enemy found"
                        else:
                            return "Game over"

        elif direction == "down":
            for elem in self.position:
                for e in elem:
                    if e == "H":
                        if self.position.index(elem) + 1 <= len(self.position) - 1:
                            if self.position[self.position.index(elem) + 1][elem.index(e)] == ".":
                                self.position[self.position.index(elem) + 1][elem.index(e)] = "H"
                                self.position[self.position.index(elem)][elem.index(e)] = "."
                                self.take_mana_when_moving()
                                return True
                            elif self.position[self.position.index(elem) + 1][elem.index(e)] == "#":
                                return False
                            elif self.position[self.position.index(elem) + 1][elem.index(e)] == "T":
                                self.position[self.position.index(elem) + 1][elem.index(e)] = "H"
                                self.position[self.position.index(elem)][elem.index(e)] = "."
                                self.take_mana_when_moving()
                                return self.pick_treasure()
                            elif self.position[self.position.index(elem) + 1][elem.index(e)] == "E":
                                return "Enemy found"
                        else:
                            return "Game over"

        elif direction == "right":
            for elem in self.position:
                for e in elem:
                    if e == "H":
                        if elem.index(e) + 1 <= len(elem) - 1:
                            if self.position[self.position.index(elem)][elem.index(e) + 1] == ".":
                                self.position[self.position.index(elem)][elem.index(e) + 1] = "H"
                                self.position[self.position.index(elem)][elem.index(e)] = "."
                                self.take_mana_when_moving()
                                return True
                            elif self.position[self.position.index(elem)][elem.index(e) + 1] == "#":
                                return False
                            elif self.position[self.position.index(elem)][elem.index(e) + 1] == "T":
                                self.position[self.position.index(elem)][elem.index(e) + 1] = "H"
                                self.position[self.position.index(elem)][elem.index(e)] = "."
                                self.take_mana_when_moving()
                                return self.pick_treasure()
                            elif self.position[self.position.index(elem)][elem.index(e) + 1] == "E":
                                return "Enemy found"
                        else:
                            return "Game over"

        elif direction == "left":
            for elem in self.position:
                for e in elem:
                    if e == "H":
                        if elem.index(e) - 1 >= 0:
                            if self.position[self.position.index(elem)][elem.index(e) - 1] == ".":
                                self.position[self.position.index(elem)][elem.index(e) - 1] = "H"
                                self.position[self.position.index(elem)][elem.index(e) + 1] = "."
                                self.take_mana_when_moving()
                                return True
                            elif self.position[self.position.index(elem)][elem.index(e) - 1] == "#":
                                return False
                            elif self.position[self.position.index(elem)][elem.index(e) - 1] == "T":
                                self.position[self.position.index(elem)][elem.index(e) - 1] = "H"
                                self.position[self.position.index(elem)][elem.index(e) + 1] = "."
                                self.take_mana_when_moving()
                                return self.pick_treasure()
                            elif self.position[self.position.index(elem)][elem.index(e) - 1] == "E":
                                return "Enemy found"
                        else:
                            return "Game over"

    def hero_attack(self, by=None):
        if by == "weapon":
            return self.hero.weapon != None
            return "weapon"
        if by == "spell":
            return self.hero.spell != None
            return "spell"



#hero = Hero("Gayster", "GaySlayer")
s = Dungeon()
print(s.print_map())
print(s.position)
s.spawn(s.hero)
print(s.print_map())
#print(s.move_hero("up"))
print(s.move_hero("down"))
#print(s.move_hero("left"))
#print(s.move_hero("right"))
print(s.print_map())
print(s.hero.mana)
print(s.hero.health)
print(s.hero_attack(by="spell"))
print(s.hero_attack(by="weapon"))
