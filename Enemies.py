class Enemy:

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

enemy = Enemy(health=0, mana=100, damage=20)
print(enemy.can_cast())
