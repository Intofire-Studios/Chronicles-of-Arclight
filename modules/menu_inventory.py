from extensions.richPresence import rpcinventoryupdate
from extensions.cmdClear import consoleClear

def menu_inventory(p):
    rpcinventoryupdate(p)
    consoleClear()
    print("---")
    print(f"{p.name}'s inventory!")
    print("---")
    print(f"Pickaxe: {p.pickaxe}/{p.max_pickaxe}")
    print(f"Sword: {p.damage} ({p.sword}/{p.max_sword})")
    print(f"Armor: {p.armor}/{p.max_armor}")
    if p.stone+p.copper+p.tin+p.iron+p.aluminum+p.gold+p.crystal+p.diamond+p.emerald+p.topaz+p.ruby+p.silver>0:
        print("---")
    if p.stone != 0:
        print(f"Stone: {p.stone}")
    if p.copper != 0:
        print(f"Сopper: {p.copper}")
    if p.tin != 0:
        print(f"Tin: {p.tin}")
    if p.iron != 0:
        print(f"Iron: {p.iron}")
    if p.aluminum != 0:
        print(f"Aluminum: {p.aluminum}")
    if p.silver != 0:
        print(f"Silver: {p.silver}")
    if p.topaz != 0:
        print(f"Topaz: {p.topaz}")
    if p.gold != 0:
        print(f"Gold: {p.gold}")
    if p.crystal != 0:
        print(f"Crystal: {p.crystal}")
    if p.diamond != 0:
        print(f"Diamond: {p.diamond}")
    if p.ruby != 0:
        print(f"Ruby: {p.ruby}")
    if p.emerald != 0:
        print(f"Emerald: {p.emerald}")
    print("---")
    input("Enter to continue.")
    consoleClear()