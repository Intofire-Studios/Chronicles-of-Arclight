import sqlite3

class Player:
    def __init__(self):
        self.connection = sqlite3.connect('saves.sqlite')
        self.cursor = self.connection.cursor()
        self.load_data()

    def load_data(self):
        self.cursor.execute("SELECT * FROM save;")
        data = self.cursor.fetchone()
        self.name = data[1]
        self.cls = data[2]
        self.hp = data[3]
        self.max_hp = data[4]
        self.heal_hp = data[5]
        self.pw = data[6]
        self.level = data[7]
        self.sp = data[8]
        self.money = data[9]
        self.xp = data[10]
        self.plus_pw = data[11]
        self.max_xp = data[12]
        self.pwpotion = data[13]
        self.hppotion = data[14]
        self.location = data[15]
        self.sandspass = data[16]
        self.snowkingdompass = data[17]

        self.cursor.execute("SELECT * FROM inventory;")
        data = self.cursor.fetchone()
        self.pickaxe = data[1]
        self.max_pickaxe = data[2]
        self.stone = data[3]
        self.copper = data[4]
        self.tin = data[5]
        self.iron = data[6]
        self.aluminum = data[7]
        self.silver = data[8]
        self.topaz = data[9]
        self.gold = data[10]
        self.crystal = data[11]
        self.diamond = data[12]
        self.emerald = data[13]
        self.ruby = data[14]
        self.sword = data[15]
        self.max_sword = data[16]
        self.damage = data[17]
        self.armor = data[18]
        self.max_armor = data[19]

    def save_data(self):
        save_query = """
            UPDATE save
            SET name=?, cls=?, hp=?, max_hp=?, heal_hp=?, pw=?, level=?, sp=?, money=?, xp=?, plus_pw=?, max_xp=?, pwpotion=?, hppotion=?, location=?, sandspass=?, snowkingdompass=?
            WHERE id=1
        """
        save_data = (self.name, self.cls, self.hp, self.max_hp, self.heal_hp, self.pw, self.level, self.sp, self.money, self.xp, self.plus_pw, self.max_xp, self.pwpotion, self.hppotion, self.location, self.sandspass, self.snowkingdompass)
        self.cursor.execute(save_query, save_data)

        inventory_query = """
            UPDATE inventory
            SET pickaxe=?, max_pickaxe=?, stone=?, copper=?, tin=?, iron=?, aluminum=?, silver=?, topaz=?, gold=?, crystal=?, diamond=?, emerald=?, ruby=?, sword=?, max_sword=?, damage=?, armor=?, max_armor=?
            WHERE id=1
        """
        inventory_data = (self.pickaxe, self.max_pickaxe, self.stone, self.copper, self.tin, self.iron, self.aluminum, self.silver, self.topaz, self.gold, self.crystal, self.diamond, self.emerald, self.ruby, self.sword, self.max_sword, self.damage, self.armor, self.max_armor)
        self.cursor.execute(inventory_query, inventory_data)

        self.connection.commit()

    def close(self):
        self.connection.close()