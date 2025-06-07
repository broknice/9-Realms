def crafting_hall(player):
    recipes = {
        "Healing Potion": {"Slime Gel": 2, "Goblin Ear": 1},
        "Toxin Vial": {"Wasp Stinger": 3, "Slime Gel": 3, "Mystic Flower": 1},
        "Ultimate Healing Potion": {"Dragon Core": 1, "Ectoplasm": 3, "Mystic Flower": 5},
        "Antidote": {"Wasp Stinger": 2, "Mystic Flower": 1},
        "Alchemist’s Fire": {"Slime Gel": 1, "Exoskeleton": 1, "Lightning Ball": 1},
        "Bonemeal": {"Bone": 10, "Exoskeleton": 5},
        "Wolf Armor": {"Werewolf Hide": 1, "Wolf Fang": 10},
        "Mystic Enhancement Potion": {"Mystic Flower": 10, "Ectoplasm": 10, "Lightning Ball": 15},
        "Dragon Force Pill": {"Mystic Flower": 10, "Ectoplasm": 10, "Dragon Core": 2}
    }

    values = {
        "Bonemeal": 100,
        "Wolf Armor": 150,
        "Mystic Enhancement Potion": 200,
        "Dragon Force Pill": 350
    }

    sell_prices = {
        "Goblin Ear": 10,
        "Wolf Fang": 12,
        "Wasp Stinger": 8,
        "Antenna": 8,
        "Spellbook: Fireball": 30,
        "Ectoplasm": 25,
        "Dragon Core": 50,
        "Mystic Flower": 15,
        "Exoskeleton": 10,
        "Lightning Ball": 20,
        "Bone": 5,
        "Werewolf Hide": 40,
        "Slime Gel": 6
    }

    print("\n🛠️ You enter the Crafting Hall and are immediately hit with heat from both blacksmith furnaces and alchemist flames.")
    print("A gruff dwarf at the counter greets you with a harrumph and a knowing smile: \"Welcome to the Crafting Hall!\"")
    print("His voice echoes over the hall, louder even than the banging of metal — but no one pays it any mind.")

    while True:
        print("\nWhat would you like to do?")
        print("1. Craft Items")
        print("2. Sell Materials")
        print("E. Exit")

        action = input("Choose an option: ").strip().lower()

        if action == "e":
            print("👋 You leave the Crafting Hall.")
            break

        elif action == "1":
            item_names = list(recipes.keys())
            print("\nAvailable Recipes:")
            for i, item in enumerate(item_names, 1):
                reqs = recipes[item]
                max_craft = min(player.inventory.get(k, 0) // v for k, v in reqs.items())
                print(f"{i}. {item} (Can craft: {max_craft})")
            print("E. Cancel")

            choice = input("Select an item to craft (1–{} or E to cancel): ".format(len(item_names))).strip().lower()

            if choice == "e":
                continue
            elif choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(item_names):
                    result = item_names[choice - 1]
                    requirements = recipes[result]

                    can_craft = all(player.inventory.get(item, 0) >= qty for item, qty in requirements.items())

                    if not can_craft:
                        print("❌ You don’t have the required ingredients:")
                        for item, qty in requirements.items():
                            owned = player.inventory.get(item, 0)
                            print(f"- {item}: {owned} / {qty}")
                        continue

                    for item, qty in requirements.items():
                        player.remove_item(item, qty)
                    player.add_item(result)

                    print(f"✅ You crafted {result}!")

                    if result in values:
                        sell_value = values[result]
                        player.remove_item(result)
                        player.earn_gold(sell_value)
                        print(f"💰 You sold {result} for {sell_value} gold!")
                else:
                    print("❌ Invalid choice.")
            else:
                print("❌ Invalid input.")

        elif action == "2":
            print(f"\n💰 You have {player.gold} gold.")
            material_list = {item: price for item, price in sell_prices.items() if item in player.inventory}

            if not material_list:
                print("You have no materials to sell.")
                continue

            print("\nSellable Materials:")
            for i, (item, price) in enumerate(material_list.items(), 1):
                qty = player.inventory[item]
                print(f"{i}. {item} (You have {qty}) - {price} gold each")
            print(f"{len(material_list)+1}. Cancel")

            choice = input("Enter the number of the item to sell: ").strip()
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(material_list):
                    item_name = list(material_list.keys())[choice - 1]
                    max_qty = player.inventory[item_name]
                    amount = input(f"How many {item_name}s would you like to sell? (Max {max_qty}): ").strip()
                    if amount.isdigit():
                        amount = int(amount)
                        if 1 <= amount <= max_qty:
                            total = sell_prices[item_name] * amount
                            player.gold += total
                            player.remove_item(item_name, amount)
                            print(f"✅ Sold {amount} x {item_name} for {total} gold.")
                        else:
                            print("❌ Invalid quantity.")
                elif choice == len(material_list) + 1:
                    continue
                else:
                    print("❌ Invalid selection.")
            else:
                print("❌ Invalid input.")

        else:
            print("❌ Invalid input.")
