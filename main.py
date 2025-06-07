# Entry point for the game

from player import Player
from combat import combat
from data.biomes import biomes
from data.monsters import goblin
from data.items import use_item
from data.classes import character_classes
from locations.gate import gate_to_wilds
from locations.alchemy import alchemy_shop
from locations.church import church
from locations.crafting import crafting_hall
from locations.tavern import tavern
from locations.guild import mercenary_guild
import random

# === Game Loop Utilities ===
def town_menu(player):
    while True:
        print("\n🏘️ Welcome to Town! Where would you like to go?")
        print("1. Tavern")
        print("2. Gate to the Wilds")
        print("3. Alchemy Shop")
        print("4. Crafting Hall")
        print("5. Church")
        print("6. Mercenary Guild")
        print("7. View Inventory")
        print("8. View Status")
        print("E. Exit Game")

        choice = input("Enter a number (1–8): ")

        if choice == "1":
            tavern(player)
        elif choice == "2":
            gate_to_wilds(player)
        elif choice == "3":
            alchemy_shop(player)
        elif choice == "4":
            crafting_hall(player)
        elif choice == "5":
            church(player)
        elif choice == "6":
            mercenary_guild(player)
        elif choice == "7":
            print("\n🎒 Inventory:")
            print(f"Gold: {player.gold}")
            print(f"HP: {player.hp}")
            if not player.inventory:
                print("Your inventory is empty.")
            else:
                for item, qty in player.inventory.items():
                    print(f"- {item}: {qty}")

                print("\nWould you like to use an item?")
                use = input("Enter the item name to use it, or press Enter to skip: ").strip()

                if use:
                    from data.items import use_item
                    use_item(player, use)

        elif choice == "8":
            player.show_status()
        elif choice == "E":
            print("\n👋 Thanks for playing! Safe travels, adventurer.")
            break
        else:
            print("\n❌ Invalid choice. Try again.")

# === Start Game ===
if __name__ == "__main__":
    print("🎮 Welcome to the RPG Character Creator!")
    name = input("Enter your character's name: ")

    print("\nChoose your class:")
    class_names = list(character_classes.keys())
    for i, cname in enumerate(class_names, 1):
        print(f"{i}. {cname} - {character_classes[cname]['Description']}")

    while True:
        class_choice = input("Enter the number of your chosen class: ")
        if class_choice.isdigit() and 1 <= int(class_choice) <= len(class_names):
            chosen_class = class_names[int(class_choice) - 1]
            break
        else:
            print("❌ Invalid choice. Please try again.")

    player = Player(name, chosen_class, character_classes[chosen_class])
    print("\n🎉 Character created!\n")
    print(player.summary())
    town_menu(player)
