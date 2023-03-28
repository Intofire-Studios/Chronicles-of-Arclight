from extensions.saveProcess import saveProcess
from extensions.cmdClear import consoleClear
from random import randint, choice
from modules.menu_upgrade import menu_upgrade
from extensions.richPresence import rpclose, rpcupdate, rpcfightupdate
from extensions.fileAssociation import saves, lastsavepath
from modules import enemies
from time import sleep
from math import ceil

def menu_fight(p):
    saveProcess(p, saves, lastsavepath)
    usedpwpotions = 0
    rpcfightupdate(p)

    if p.location == "spawn":
        enemy = choice(enemies.enemy_spawn["regular"] + enemies.enemy_spawn["normal"] + enemies.enemy_spawn["boss"])

        if enemy in enemies.enemy_spawn["regular"]:
            ehp = randint(10,20) + ceil(p.max_hp * 0.33)
            epw = 2 * randint(1,5) + ceil(p.pw * 0.25)
        elif enemy in enemies.enemy_spawn["normal"]:
            ehp = randint(30,50) + ceil(p.max_hp * 0.33)
            epw = 2 * randint(3,7) + ceil(p.pw * 0.25)
        elif enemy in enemies.enemy_spawn["boss"]:
            ehp = randint(75,100) + ceil(p.max_hp * 0.33)
            epw = 2 * randint(5,10) + ceil(p.pw * 0.25)
    elif p.location == "sands":
        enemy = choice(enemies.enemy_sands["regular"] + enemies.enemy_sands["normal"] + enemies.enemy_sands["boss"])

        if enemy in enemies.enemy_sands["regular"]:
            ehp = randint(30,50) + ceil(p.max_hp * 0.5)
            epw = 2 * randint(2,10) + ceil(p.pw * 0.5)
        elif enemy in enemies.enemy_sands["normal"]:
            ehp = randint(55,95) + ceil(p.max_hp * 0.5)
            epw = 2 * randint(4,12) + ceil(p.pw * 0.5)
        elif enemy in enemies.enemy_sands["boss"]:
            ehp = randint(100,130) + ceil(p.max_hp * 0.5)
            epw = 2 * randint(10,20) + ceil(p.pw * 0.5)
    elif p.location == "snow kingdom":
        enemy = choice(enemies.enemy_snow_kingdom["regular"] + enemies.enemy_snow_kingdom["normal"] + enemies.enemy_snow_kingdom["boss"])

        if enemy in enemies.enemy_snow_kingdom["regular"]:
            ehp = randint(40,60) + ceil(p.max_hp * 0.5)
            epw = 2 * randint(4,15) + ceil(p.pw * 0.5)
        elif enemy in enemies.enemy_snow_kingdom["normal"]:
            ehp = randint(70,100) + ceil(p.max_hp * 0.5)
            epw = 2 * randint(6,20) + ceil(p.pw * 0.5)
        elif enemy in enemies.enemy_snow_kingdom["boss"]:
            ehp = randint(120,150) + ceil(p.max_hp * 0.5)
            epw = 2 * randint(15,30) + ceil(p.pw * 0.5)

    enemy = enemy.capitalize()

    consoleClear()
    while ehp > 0:
        print("---")
        print(f"{enemy}: {ehp}. Power: {epw}")
        print(f"{p.name}: {p.hp}/{p.max_hp}. Power: {p.pw}. Sword: {p.damage} ({p.sword}/{p.max_sword}). Armor: {p.armor}/{p.max_armor}")
        print("---")
        print(f"1. Punch with power {p.pw+p.sword}")
        print(f"2. Use heal potion (+{p.heal_hp}) ({p.hppotion} left)")
        print(f"3. Use power potion (+{p.plus_pw}) ({p.pwpotion} left)")
        print("4. Run away!")
        n = input("Number: ")
        if n == "1":
            r = randint(1,2)
            if r == 1:
                if p.sword > 0:
                    ehp -= p.pw+p.damage
                    p.sword -= 1
                else:
                    ehp -= p.pw
                consoleClear()
                print("---")
                print("You hit the enemy!")
                rpcfightupdate(p)
            if r == 2:
                if p.armor>0:
                    p.armor -= 1
                    p.hp -= ceil(epw*0.25)
                else:
                    p.hp -= ceil(epw)
                consoleClear()
                print("---")
                print("Enemy hit you!")
                rpcfightupdate(p)
                if p.hp <= 0:
                    consoleClear()
                    print("---")
                    print("You've lost!")
                    print("---")
                    rpclose(p)
                    sleep(5)
                    exit()
        if n == "2":
            consoleClear()
            if p.hppotion > 0:
                consoleClear()
                p.hppotion -= 1
                p.hp += p.heal_hp
                if p.hp > p.max_hp:
                    p.hp = p.max_hp
                consoleClear()
                print("---")
                print(f"Healing... {p.hp}")
                rpcfightupdate(p)
            else:
                print("---")
                print("Not enough potions!")
        if n == "3":
            consoleClear()
            if p.pwpotion > 0:
                consoleClear()
                usedpwpotions += 1
                p.pwpotion -= 1
                p.pw += p.plus_pw
                print("---")
                print(f"Drinking the potion... {p.pw}")
                rpcfightupdate(p)
            else:
                print("---")
                print("Not enough potions!")
        if n == "4":
            r = randint(1,4)
            if r == 3:
                consoleClear()
                print("---")
                print("You ran away!")
                print("---")
                sleep(3)
                return True
            else:
                consoleClear()
                print("---")
                print("You can't run!")
            rpcfightupdate(p)
    if usedpwpotions != 0:
        p.pw -= usedpwpotions * p.plus_pw
    rpcfightupdate(p)

    if p.location == "sands":
        p.xp += 3
    elif p.location == "snow kingdom":
        p.xp += 5
    elif p.location == "spawn":
        p.xp += 1
    p.sp += 1
    p.money += 1

    r = randint(1, 100)
    if r == 100 and p.sandspass == 0 and p.location == "spawn":
        p.sandspass = 1

    ch = randint(1, 250)
    if ch == 250 and p.snowkingdompass == 0 and p.location == "sands":
        p.snowkingdompass = 1

    if p.xp >= p.max_xp:
        p.xp = 0
        p.max_xp *= 5
        p.level += 1
        p.sp += 2
        menu_upgrade(p)