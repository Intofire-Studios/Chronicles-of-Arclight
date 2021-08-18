from modules.shop_pages.passes import menu_passes
from modules.shop_pages.potions import menu_potions
from extensions.cfgSave import cfgsave
from extensions.cmdClear import consoleClear
from extensions.richPresence import rpcshopupdate

def menu_shop(p):
    cfgsave(p, 'saves.ini')
    rpcshopupdate(p)
    consoleClear()
    while p.money > 0:
        cfgsave(p, 'saves.ini')
        print("---")
        print("Choose a category! Money: {}".format(p.money))
        print("---")
        print("1. Potions")
        print("2. Travel passes")
        print("3. Exit to main menu")
        n = input("Number: ")
        consoleClear()
        if n == "1":
            menu_potions(p)
        if n == "2":
            menu_passes(p)
        if n == "3":
            break
    consoleClear()
    cfgsave(p, 'saves.ini')