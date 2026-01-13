# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return f'{self.name}'
# my_cat = Cat('mye')
# print(my_cat.speak())
# my_cat.name = 'Barsik'
# print(my_cat.name)

# class Fury:
#     pass
#     def __init__(self, name):
#         self.name = name
#         self.health = 324
#     def skills(self):
#         return f'{self.name} is using abillity <spark>...'
# f1 = Fury('Arc Warden')
# print(f1.name)
# print(f1.health)
# print(f1.skills())

print('dota3\n')
class Hero:
    def __init__(self, name, health=100, max_health=None, damage=53):
        self.name = name
        self.health = health
        self.max_health = health or max_health
        self.damage = damage

    def stutus(self):
        precent =(self.health / self.max_health) * 100
        return f'{self.name}: {self.health} / {self.max_health} hp ({precent:.0f}%) | Damage: {self.damage}'

    def main_attack(self, target):
        return f'{self.name} is attacking {target.name} by {self.damage}'

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return f'{self.name} take {damage} damage, your health now: {self.health} hp'

    def is_alive(self):
        return self.health > 0
class Hero2:
    def __init__(self, name, health=550, damage=68):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage

    def stutus(self):
        precent = (self.health / self.max_health) * 100
        return f'{self.name}: {self.health} / {self.max_health} hp ({precent:.0f}%) | Damage: {self.damage}'

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return f'{self.name} take {damage} damage, your health now: {self.health} hp'

    def is_alive(self):
        return self.health > 0

player1 = Hero('Invoker', 678, damage=870)
player6 = Hero('Ogr Magi', 859, 65)
player7 = Hero('Timbersaw', 761, 59)

lobby = [player1, player6, player7]

print(20*'=', 'Lobby:', 20*'=')
for unit in lobby:
    print(unit.stutus())
print('=' * 48 + '\n')

def battle(attacker, defender):
    print(f'\nFirst battle')
    print(attacker.stutus())
    print(defender.stutus())

    print(attacker.main_attack(defender))
    print(defender.take_damage(attacker.damage))

    print(defender.stutus())
    print('-'*30)

battle(player6, player1)
battle(player1, player6)
battle(player7, player1)
battle(player1, player7)

print('End.')
for unit in lobby:
    status = unit.stutus()
    if not unit.is_alive():
        status += ' / Dead'
    print(status)