f = open("input21.txt","r")
lines = f.readlines()

boss_damage = 8
boss_armour = 2

my_damage = ?
my_armour = ?

my_hit = max(my_damage-boss_armour,1)
boss_hit = max(boss_damage-my_armour,1)

# Solved with some arithmetic !

