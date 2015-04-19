from weapon import Weapon
from spell import Spell


class Hero:

    def __init__(self, name, title, health=100, mana=50, mana_regeneration_rate=2):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self. mana_regeneration_rate = mana_regeneration_rate
        self.weapon = None
        self.spell = None

    def known_as(self):
        message = "{} the {}"
        return message.format(self.name, self.title)

    def is_alive(self):
        if self.health != 0:
            return True
        return False

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def can_cast(self):
        return self.mana != 0

    def take_damage(self, damage_points):
        if self.health - damage_points > 0:
            self.health -= damage_points
        else:
            self.health = 0

    def take_healing(self, healing_points):
        if self.is_alive() is False:
            return False
        elif self.health + healing_points < 100:
            self.health += healing_points
        else:
            self.health = 100

    def take_mana(self, mana_points=0):
        if self.mana + mana_points <= 50:
            self.mana += mana_points

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def attack(self, by=''):
        if by == "weapon":
            return self.weapon.get_weapon_damage()
        elif by == "spell":
            return self.spell.get_spell_damage()
        else:
            return 0


hero = Hero("Gayster", "GaySlayer")
#w = Weapon(name="The Axe of Destiny", damage=20)
s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)

print(hero.known_as())
hero.take_damage(50)
hero.take_healing(60)
print(hero.health)
hero.learn(s)
hero.equip(Weapon(name="The Axe of Destiny", damage=20))
print(hero.attack(by="spell"))
print(hero.attack(by="weapon"))
hero.take_mana(100)
print(hero.mana)
