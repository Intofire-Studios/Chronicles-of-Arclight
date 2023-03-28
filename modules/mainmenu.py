from modules.menu_inventory import menu_inventory
from modules.menu_mine import menu_mine
from modules.menu_location import menu_location
from extensions.richPresence import rpcupdate
from modules.menu_upgrade import menu_upgrade
from modules.menu_stats import menu_stats
from modules.menu_fight import menu_fight
from modules.menu_craft import menu_craft
from extensions.saveProcess import saveProcess
from extensions.cmdClear import consoleClear
from extensions.fileAssociation import saves, lastsavepath
from extensions.versionChecker import versionChecker, updaterChecker
from extensions.dlala import dlala
from modules.menu_shop import menu_shop
import os, time
import requests

def mainmenu(p):
    while True:
        saveProcess(p, saves, lastsavepath)
        lastsave = os.path.getmtime(saves)
        updaterChecker()
        consoleClear()
        rpcupdate(p)
        if versionChecker() == 1:
            print("---")
            print('New version is available!', 'Download here — https://github.com/Intofire-Studios/Chronicles-of-Archlight/releases')
            print('')
            info = requests.get('https://raw.githubusercontent.com/Intofire-Studios/Chronicles-of-Archlight/master/extensions/version.txt')
            with open('extensions/version.txt', 'r') as f:
                print(f'Current version: {f.read()[9:-1]}')
            print(f'New version: {str(info.content)[11:-3]}')
        elif versionChecker() == 2:
            print("---")
            with open('extensions/version.txt', 'r') as f:
                print(f'v{f.read()[9:-1]} beta.')
        print("---")
        print("Choose what to do!")
        print("---")
        if versionChecker() == 1:
            print('0. Download the update')
        print("1. Go fight!")
        if p.max_pickaxe != 0:
            print(f"2. Go to the mine!        | Pickaxe: {p.pickaxe}/{p.max_pickaxe}")
        else:
            print("2. <CLOSED>")
        print(f"3. Check your stats       | HP: {p.hp}/{p.max_hp} | Power: {p.pw}")
        print("4. Check your inventory")
        if p.sp > 0:
            print(f"5. Upgrade your character | Skill Points: {p.sp}")
        else:
            print("5. <CLOSED>")
        print(f"6. Open shop              | Money: {p.money}")
        if p.stone+p.copper+p.tin+p.iron+p.aluminum+p.gold+p.crystal+p.diamond+p.emerald+p.topaz+p.ruby+p.silver>0:
            print("7. Open craft menu")
        else:
            print("7. <CLOSED>")
        print(f"8. Change your location   | Current location: {p.location.capitalize()}")
        print(f"9. Close the game         | Last save: {time.ctime(lastsave)}")
        n = input("Number: ")
        if n == '0' and versionChecker() == 1:
            os.system('python updater/updater.py')
            exit()
        if n == "1":
            menu_fight(p)
        if n == "2":
            menu_mine(p)
        if n == "3":
            menu_stats(p)
        if n == "4":
            menu_inventory(p)
        if n == "5":
            menu_upgrade(p)
        if n == "6":
            menu_shop(p)
        if n == "7":
            menu_craft(p)
        if n == "8":
            menu_location(p)
        if n == "9":
            consoleClear()
            print("Closing the game...")
            saveProcess(p, saves, lastsavepath)
            time.sleep(3)
            consoleClear()
            exit()
        #if n.lower() == "dlala":
        #    dlala(p)