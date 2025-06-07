class Player:
    def __init__(self, name, chosen_class, class_data):
        self.name = name
        self.class_name = chosen_class
        self.hp = class_data["Base HP"]
        self.mp = class_data["Base MP"]
        self.strength = class_data["Strength"]
        self.intelligence = class_data["Intelligence"]
        self.agility = class_data["Agility"]
        self.special_ability = class_data["Special Ability"]
        self.description = class_data["Description"]
        self.level = 1
        self.exp = 0
        self.gold = 50
        self.inventory = {"Healing Potion": 2}
        self.spells_learned = []
        self.current_quest = None

    def summary(self):
        return {
            "Name": self.name,
            "Class": self.class_name,
            "Level": self.level,
            "EXP": self.exp,
            "HP": self.hp,
            "MP": self.mp,
            "Strength": self.strength,
            "Intelligence": self.intelligence,
            "Agility": self.agility,
            "Special Ability": self.special_ability,
            "Description": self.description,
            "Gold": self.gold,
            "Inventory": self.inventory,
            "Spells Learned": self.spells_learned
        }

    def add_item(self, item_name, amount=1):
        if item_name in self.inventory:
            self.inventory[item_name] += amount
        else:
            self.inventory[item_name] = amount

    def remove_item(self, item_name, amount=1):
        if item_name in self.inventory and self.inventory[item_name] >= amount:
            self.inventory[item_name] -= amount
            if self.inventory[item_name] == 0:
                del self.inventory[item_name]
            return True
        return False

    def spend_gold(self, amount):
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False

    def earn_gold(self, amount):
        self.gold += amount

    def gain_exp(self, amount):
        self.exp += amount
        print(f"\u2728 You gained {amount} EXP!")

        exp_to_next = self.level * 100
        if self.exp >= exp_to_next:
            self.level_up()

    def show_status(self):  # <- define inside the class!
        print("\n📊 === Player Status ===")
        print(f"Name: {self.name}")
        print(f"Class: {self.class_name}")
        print(f"Level: {self.level}")
        exp_to_next = self.level * 100
        print(f"EXP: {self.exp} / {exp_to_next}")
        print(f"HP: {self.hp}")
        print(f"MP: {self.mp}")
        print(f"Strength: {self.strength}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Agility: {self.agility}")
        print(f"Gold: {self.gold}")
        print(f"Inventory: {self.inventory}")
        if self.spells_learned:
            print(f"🧙 Spells Learned: {', '.join(self.spells_learned)}")
        else:
            print("🧙 Spells Learned: None")

        if self.current_quest:
            print(f"📜 Quest: {self.current_quest['name']}")
            print(f"Progress: {self.current_quest['progress']} / {self.current_quest['goal']}")
        else:
            print("📜 Quest: None")
        print("=========================\n")

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.hp = 100 + self.level * 5
        self.mp += 5
        self.strength += 2
        self.intelligence += 2
        self.agility += 1
        print("💪 Your level have increased.")
        print("\u2728 Your stats have increased.")
    
