import itertools

my_hit_points = 50
my_mana = 500

boss_hit_points = 51
boss_damage = 9

attacks = ['Magic Missile','Drain','Shield','Poison','Recharge']

combs = itertools.product(attacks,repeat=9)

min_mana_needed = 99999999999

for comb in combs:
    game_my_hit_points = my_hit_points
    game_my_mana = my_mana
    game_my_armour = 0
    game_boss_hit_points = boss_hit_points
    mana_used = 0
    won = False
    shield_count = 0
    poison_count = 0
    recharge_count = 0

    for attack in comb:
        # Check the effects
        if shield_count > 1:
            shield_count -= 1
        elif shield_count == 1:
            shield_count -= 1
            game_my_armour = 0

        if poison_count > 0:
            game_boss_hit_points -= 3
            poison_count -= 1

        if recharge_count > 0:
            game_my_mana += 101
            recharge_count -= 1

        if game_boss_hit_points <= 0:
            won = True
            break

        # Now have my turn
        # PART B HARD MODE
        game_my_hit_points -= 1
        # Check game over
        if game_my_hit_points <= 0:
            break

        if attack == "Magic Missile":
            if game_my_mana < 53:
                # out of mana
                break
            else:
                game_my_mana -= 53
                mana_used += 53
                game_boss_hit_points -= 4
        elif attack == "Drain":
            if game_my_mana < 73:
                break
            else:
                game_my_mana -= 73
                mana_used += 73
                game_boss_hit_points -= 2
                game_my_hit_points += 2
        elif attack == "Shield":
            if shield_count > 0:
                # Cannot have shield start while shield still active!
                break
            else:
                if game_my_mana < 113:
                    break
                else:
                    game_my_mana -= 113
                    mana_used += 113
                    shield_count = 6
                    game_my_armour = 7
        elif attack == "Poison":
            if poison_count > 0:
                # Cannot have poison start while poison still active!
                break
            else:
                if game_my_mana < 173:
                    break
                else:
                    game_my_mana -= 173
                    mana_used += 173
                    poison_count = 6
        elif attack == "Recharge":
            if recharge_count > 0:
                # Cannot have recharge start while recharge still active!
                break
            else:
                if game_my_mana < 229:
                    break
                else:
                    game_my_mana -= 229
                    mana_used += 229
                    recharge_count = 5

        # Check game over
        if game_boss_hit_points <= 0:
            won = True
            break

        # Now do effects again
        if shield_count > 1:
            shield_count -= 1
        elif shield_count == 1:
            shield_count -= 1
            game_my_armour = 0

        if poison_count > 0:
            game_boss_hit_points -= 3
            poison_count -= 1

        if recharge_count > 0:
            game_my_mana += 101
            recharge_count -= 1

        # Check game over
        if game_boss_hit_points <= 0:
            won = True
            break

        # Finally do boss move
        game_my_hit_points -= (boss_damage - game_my_armour)

        # Check game over
        if game_my_hit_points <= 0:
            break

    if won:
        min_mana_needed = min(min_mana_needed,mana_used)

print("Min mana:",min_mana_needed)