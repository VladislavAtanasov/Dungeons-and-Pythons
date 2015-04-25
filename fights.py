from Our_Hero import Hero
from enemy import Enemy
#from dungeon import Dungeon
from spell import Spell
from weapon import Weapon
import random


class Fight:

    def __init__(self, hero, enemy):
        self.result = None
        self.hero = hero
        self.enemy = enemy
        #self.dungeon = Dungeon("map.txt")
        self.treasures = {"mana": [10, 15, 20, 30],
                            "health": [10, 12, 17, 23],
                            "weapon": [Weapon("Axe", 20), Weapon("Water sword", 40)],
                            "spell": [Spell("low_level", 10, 20, 1), Spell("strong", 30, 30, 6)]
                            }

    def enemy_learn_spell_escape(self):
        if self.enemy.health < 75:
            self.enemy.learn(random.choice(self.treasures["spell"]))
            return True
        else:
            return False

    def hero_attacks(self):
        if self.hero.weapon != None and self.hero.spell != None:
            if self.hero.attack(by="spell") > self.hero.attack(by="weapon"):
                self.hero.mana =- self.hero.spell.mana_cost
                self.enemy.take_damage(self.hero.spell.damage)
                return("Hero casts a {}, hits enemy for {} dmg. Enemy health is {}.").format(self.hero.spell.name, self.hero.spell.damage, self.enemy.health)
            elif self.hero.can_cast():
                self.enemy.take_damage(self.hero.weapon.damage)
                return("Hero attacks with {}, hits enemy for {} dmg. Enemy health is {}.").format(self.hero.weapon.name, self.hero.weapon.damage, self.enemy.health)
            else:
                self.enemy.take_damage(self.hero.weapon.damage)
                return("Hero does not have mana for another {}. Hero attacks with {}, enemy health is".format(self.hero.spell.name, self.hero.weapon.name, self.enemy.health))
        elif self.hero.weapon != None:
            self.enemy.take_damage(self.hero.weapon.damage)
            return("Hero attacks with {}, hits enemy for {} dmg. Enemy health is {}.").format(self.hero.weapon.name, self.hero.weapon.damage, self.enemy.health)
        else:
            self.hero.mana =- self.hero.spell.mana_cost
            self.enemy.take_damage(self.hero.spell.damage)
            return("Hero casts a {}, hits enemy for {} dmg. Enemy health is {}.").format(self.hero.spell.name, self.hero.spell.damage, self.enemy.health)

    def enemy_attacks(self):
        if self.enemy_learn_spell_escape():
            if self.enemy.can_cast():
                self.hero.take_damage(self.enemy.spell.damage)
                self.enemy.mana -= self.enemy.spell.mana_cost
                return "Enemy attacks with {} for {} dmg. Hero health is {}.".format(self.enemy.spell.name, self.enemy.spell.damage, self.hero.health)
            else:
                self.hero.take_damage(self.enemy.damage)
                return "Enemy hits hero for {} dmg. Hero health is {}.".format(self.enemy.damage, self.hero.health)
        else:
            self.hero.take_damage(self.enemy.damage)
            return "Enemy hits hero for {} dmg. Hero health is {}.".format(self.enemy.damage, self.hero.health)

    def start_attack(self):
        #if self.dungeon.move_hero("up") == "Enemy found" or self.dungeon.move_hero("down") == "Enemy found" or self.dungeon.move_hero("left") == "Enemy found" or self.dungeon.move_hero("right") == "Enemy found":
        print("A fight has started between our Hero({} {}) and Enemy({} {}).".format(self.hero.name, self.hero.health, self.enemy.damage, self.enemy.health))
        while self.hero.health > 0 and self.enemy.health > 0:
            print(self.hero_attacks())
            if self.enemy.health == 0:
                return "Enemy is dead!"
            else:
                print(self.enemy_attacks())
                if self.hero.health == 0:
                    return "Our Hero died..."



#s = Dungeon()
f = Fight(Hero("Gaysters", "Gayslayer"), Enemy(100, 60, 20))
w = Weapon("Axeee", 10)
s = Spell("Fireball", 20, 30, 2)
f.hero.equip(w)
f.hero.learn(s)
#print(f.start_attack())
