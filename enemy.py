from spell import Spell
from weapon import Weapon

class Enemy:

    def __init__(self, health, mana, damage):
        self.health = health
        self.mana = mana
        self.damage = damage
        self.weapon = None
        self.spell = None

    def is_alive(self):
        return self.health != 0

    def can_cast(self):
        return self.mana != 0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, healing_points):
        if self.health == 0:
            return False
        elif self.health - healing_points >= 0:
            self.health += healing_points
            return True
        else:
            raise ValueError("Too small initial health")

    def take_mana(self, mana_points):
        current_mana = self.mana
        if self.mana - mana_points >= 0:
            self.mana += mana_points
        if self.mana > current_mana:
            self.mana = current_mana

    def take_damage(self, damage_points):
        self.health -= damage_points

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def attack(self, by):
        if by == "weapon":
            return self.weapon.get_weapon_damage()
        elif by == "spell":
            return self.spell.get_spell_damage()


enemy = Enemy(100, 10, 20)
w = Weapon("Axe", 10)
s = Spell("Stick", 10, 20, 2)
enemy.equip(w)
print enemy.attack(by="weapon")
