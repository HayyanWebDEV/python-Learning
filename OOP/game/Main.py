from player import Player
from enemy import Enemy

hayyan = Player("hayyan")
print(hayyan)
hayyan.lives -= 1
print(hayyan)
hayyan.lives -= 1
print(hayyan)
hayyan.level += 2
print(hayyan)
hayyan.level += 1
print(hayyan)
hayyan.level += 3
print(hayyan)

enemy = Enemy()
while enemy.lives:
    enemy.take_damage(1)
    print(enemy)
