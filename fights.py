from Our_Hero import Hero
from enemy import Enemy
from dungeon import Dungeon
from spell import Spell
from weapon import Weapon


class Fight:

    def __init__(self):
        self.result = None
        self.dungeon = Dungeon()
        self.hero = Hero("Gayster", "GaySlayer", 50, 20)

    def hero_attack_range(self):
        if self.dungeon.hero_attack():
            if self.hero.spell != None:
                if self.dungeon.move_hero("up") == True:
                    if self.dungeon.move_hero("up") == "Enemy Found":
                        return "Start fight"

                elif self.dungeon.move_hero("down") == True:
                    if self.dungeon.move_hero("down") == "Enemy Found":
                        return "Start fight"

                elif self.dungeon.move_hero("left") == True:
                    if self.dungeon.move_hero("left") == "Enemy Found":
                        return "Start fight"

                elif self.dungeon.move_hero("right") == True:
                    if self.dungeon.move_hero("right") == "Enemy Found":
                        return "Start fight"
                else:
                    return "Nothing in range 2 found"
        else:
            return "Ok"



#s = Dungeon()
f = Fight()
print(f.hero_attack_range())
