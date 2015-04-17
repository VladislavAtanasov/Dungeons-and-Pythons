class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Spell:

    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

class Enemy(Weapon, Spell):

    def __init__(self, health, mana, damage):
        self.health = health
        self.mana = mana
        self.damage = damage

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
        self.damage = Weapon.damage
        return Weapon.damage

    def learn(self, spell):
        pass

    #def attack(self, by):
    #    if by == "Weapon":
    #        return self.equip(weapon)
    #    elif by == "Magic":
    #        return learn(spell)

enemy = Enemy(health=0, mana=100, damage=20)
print(enemy.mana)
print(enemy.take_mana(10))
print(enemy.mana)
