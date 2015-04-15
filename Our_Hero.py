class Our_Hero:

    def __init__(self, name, title, health = 100, mana = 50, mana_regeneration_rate = 2):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self. mana_regeneration_rate = mana_regeneration_rate

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
        if self.mana != 0:
            return True
        return False

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



hero = Our_Hero("Gayster", "GaySlayer")
print(hero.known_as())
hero.take_damage(50)
hero.take_healing(60)
print(hero.health)


