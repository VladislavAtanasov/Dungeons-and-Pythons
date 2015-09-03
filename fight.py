from Our_Hero import Weapon, Spell, Our_Hero
from Enemies import Enemy
from random import *

class Fight:

    def __init__(self, hero, enemy):
        self.result = None
        self.hero = hero
        self.enemy = enemy
        self.treasures = {"mana": [10, 15, 20, 30],
                            "health": [10, 12, 17, 23],
                            "weapon": [Weapon("Axe", 20), Weapon("Water sword", 40)],
                            "spell": [Spell("low_level", 10, 20, 1), Spell("strong", 30, 30, 6)]
                            }

    def enemy_learn_spell_escape(self):
        if self.enemy.health < 75:
            self.enemy.learn(choice(self.treasures["spell"]))
            return True
        else:
            return False

    def hero_attacks(self):
        if self.hero.weapon != None and self.hero.spell != None:
            if self.hero.attack(by="spell") > self.hero.attack(by="weapon"):
                self.hero.mana -= self.hero.spell.mana_cost
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
            self.hero.mana -= self.hero.spell.mana_cost
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
        print("A fight has started between our Hero({} {}) and Enemy({} {}).".format(self.hero.name, self.hero.health, self.enemy.damage, self.enemy.health))
        while self.hero.health > 0 and self.enemy.health > 0:
            print(self.hero_attacks())
            if self.enemy.health <= 0:
                print("Enemy is dead!")
                return True
        else:
            print(self.enemy_attacks())
            if self.hero.health == 0:
                print("Our Hero died...")
        self.enemy.health = 100



f = Fight(Our_Hero("Gaysters", "Gayslayer"), Enemy(100, 60, 20))
w = Weapon("Axeee", 10)
s = Spell("Fireball", 20, 30, 2)
f.hero.equip(w)
f.hero.learn(s)

    #def __init__(self):
    #    #self.hero = Our_Hero("Gayster", "GaySlayer")
    #    #self.enemy = Enemy(health=100, mana=100, damage=20)
    #    super(Fight,self).__init__()
    #def __str__(self):
    #    return "A fight is started between our Hero(health= {}, mana= {}) and Enemy(health= {}, mana= {}, damage= {})".format(self.hero.health, self.hero.mana, self.enemy.health,self.enemy.mana, self.enemy.damage)
#
#    #def atk_spell(self, hero_health):
#    #    return "Hero casts a {}, hits enemy for {} dmg. Enemy health is {}\nEnemy hits hero for {} dmg. Hero health is {}".format(self.hero.spell.name, self.hero.spell.damage, self.hero.health, self.enemy.damage,hero_health)
#
#    #def atk_weapon(self, hero_health):
#    #    return "Hero hits with {} for {} dmg. Enemy health is {}\nEnemy hits hero for {} dmg. Hero health is {}.".format(self.hero.weapon.name, self.hero.weapon.damage, self.enemy.health,self.enemy.damage,hero_health)
#
#    #def is_alive(self, health):
#    #    return health > 0
#
#    #def is_enemy_alive(self):
#    #    return self.enemy.health != 0
#
#    #def fight(self):
#    #    if self.hero.spell != None and self.hero.weapon != None:
#    #        while self.hero.mana != 0:
#    #            if self.hero.spell.damage > self.hero.weapon.damage:
#    #                new_hero_health = self.hero.health - self.enemy.damage
#    #                self.atk_spell(new_hero_health)
#    #                self.hero.mana -= self.hero.spell.mana_cost
#    #                new_enemy_health = self.enemy.health - self.hero.spell.damage
#    #                if self.is_enemy_alive(new_enemy_health) == False:
#    #                    return "Enemy is dead"
#    #                if self.is_alive(new_hero_health) == False:
#    #                    return "Hero is dead"
#    #            elif self.hero.spell.damage == self.hero.weapon.damage and self.hero.spell.mana_cost > self.hero.mana:
#    #                new_hero_health = self.hero.health - self.enemy.damage
#    #                self.atk_weapon(new_hero_health)
#    #                self.hero.mana -= self.hero.weapon.mana_cost
#    #                new_enemy_health = self.enemy.health - self.hero.weapon.damage
#    #                if self.is_enemy_alive(new_enemy_health) == False:
#    #                    return "Enemy is dead"
#    #                if self.is_alive(new_hero_health) == False:
#    #                    return "Hero is dead"
#    #            elif self.hero.spell.damage == self.hero.weapon.damage:
#    #                new_hero_health = self.hero.health - self.enemy.damage
#    #                self.atk_spell(new_hero_health)
#    #                self.hero.mana -= self.hero.spell.mana_cost
#    #                new_enemy_health = self.enemy.health - self.hero.spell.damage
#    #                if self.is_enemy_alive(new_enemy_health) == False:
#    #                    return "Enemy is dead"
#    #                if self.is_alive(new_hero_health) == False:
#    #                    return "Hero is dead"
#    #            elif self.hero.spell.damage < self.hero.weapon.damage:
#    #                new_hero_health = self.hero.health - self.enemy.damage
#    #                self.atk_weapon(new_hero_health)
#    #                self.hero.mana -= self.hero.weapon.mana_cost
#    #                new_enemy_health = self.enemy.health - self.hero.weapon.damage
#    #                if self.is_enemy_alive(new_enemy_health) == False:
#    #                    return "Enemy is dead"
#    #                if self.is_alive(new_hero_health) == False:
#    #                    return "Hero is dead"
#    #        return "Hero does not have mana for another attack."
#    #    elif self.hero.spell != None:
#    #        while self.hero.mana != 0:
#    #                new_hero_health = self.hero.health - self.enemy.damage
#    #                self.atk_spell(new_hero_health)
#    #                self.hero.mana -= self.hero.spell.mana_cost
#    #                new_enemy_health = self.enemy.health - self.hero.spell.damage
#    #                if self.is_enemy_alive(new_enemy_health) == False:
#    #                    return "Enemy is dead"
#    #                if self.is_alive(new_hero_health) == False:
#    #                    return "Hero is dead"
#    #        return "Hero does not have mana for another attack."
#    #    elif self.hero.weapon != None:
#    #        while self.hero.mana != 0:
#    #                new_hero_health = self.hero.health - self.enemy.damage
#    #                self.atk_weapon(new_hero_health)
#    #                self.hero.mana -= self.hero.weapon.mana_cost
#    #                new_enemy_health = self.enemy.health - self.hero.weapon.damage
#    #                if self.is_enemy_alive(new_enemy_health) == False:
#    #                    return "Enemy is dead"
#    #                if self.is_alive(new_hero_health) == False:
#    #                    return "Hero is dead"
    #        return "Hero does not have mana for another attack."

