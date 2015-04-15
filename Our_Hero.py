class Our_Hero:

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self. mana_regeneration_rate = mana_regeneration_rate

    def known_as(self):
        message = "{} the {}"
        return message.format(self.name, self.title)

hero = Our_Hero("Gayster", "GaySlayer", 100, 50, 2)
print(hero.known_as())


