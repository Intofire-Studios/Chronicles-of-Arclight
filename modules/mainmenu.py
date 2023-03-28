import os
import time
import requests

from extensions.cmdClear import consoleClear
from extensions.fileAssociation import saves, lastsavepath
from extensions.richPresence import rpcupdate
from extensions.saveProcess import saveProcess
from extensions.versionChecker import check_version
#, updaterChecker
from modules.menu_craft import menu_craft
from modules.menu_fight import menu_fight
from modules.menu_inventory import menu_inventory
from modules.menu_location import menu_location
from modules.menu_mine import menu_mine
from modules.menu_shop import menu_shop
from modules.menu_stats import menu_stats
from modules.menu_upgrade import menu_upgrade

def print_version_info():
    repository_url = 'https://github.com/Intofire-Studios/Chronicles-of-Arclight'
    if check_version():
        print('New version is available!', f'Download here — {repository_url}/releases')
        print('')
        info = requests.get(f'https://raw.githubusercontent.com/Intofire-Studios/Chronicles-of-Arclight/master/extensions/version.txt')
        with open('extensions/version.txt', 'r') as f:
            print(f'Current version: {f.read()[9:-1]}')
            print(f'New version: {str(info.content)[11:-3]}')

def print_menu(p):
    """Выводит главное меню и информацию о персонаже"""
    rpcupdate(p)
    print("---")
    print("Choose what to do!")
    print("---")
    print(f"{'0. Download the update' if check_version() else ''}")
    print(f"1. Go fight!")
    if p.pickaxe != 0:
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
    if p.stone + p.copper + p.tin + p.iron + p.aluminum + p.gold + p.crystal + p.diamond + p.emerald + p.topaz + p.ruby + p.silver > 0:
        print("7. Open craft menu")
    else:
        print("7. <CLOSED>")
    print(f"8. Change your location   | Current location: {p.location.capitalize()}")
    print(f"9. Close the game         | Last save: {time.ctime(os.path.getmtime(saves))}")
    print('')

def mainmenu(p):
    """Отображает главное меню и обрабатывает ввод пользователя"""
    while True:
        consoleClear()
        saveProcess(p, saves, lastsavepath)
        print_version_info()
        print_menu(p)
        options = {
            '0': lambda: os.system('python updater/updater.py') if check_version() else None,
            '1': lambda: menu_fight(p),
            '2': lambda: menu_mine(p) if p.max_pickaxe != 0 else None,
            '3': lambda: menu_stats(p),
            '4': lambda: menu_inventory(p),
            '5': lambda: menu_upgrade(p) if p.sp > 0 else None,
            '6': lambda: menu_shop(p),
            '7': lambda: menu_craft(p) if p.stone+p.copper+p.tin+p.iron+p.aluminum+p.gold+p.crystal+p.diamond+p.emerald+p.topaz+p.ruby+p.silver>0 else None,
            '8': lambda: menu_location(p),
            '9': lambda: exit(),
        }
        option = input("Number: ")
        options.get(option, lambda: None)()