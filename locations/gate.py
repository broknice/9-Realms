# === Gate to the Wilds ===

import random
from combat import combat
from data.biomes import biomes

def gate_to_wilds(player):
    if player.hp <= 0:
        print("❌ You're too injured to journey into the wilds. Visit the Church to heal first.")
        return

    print("\n🌬️ You step through the towering Gates to the Wilds and are immediately struck by a rush of air—pressure from the swirling portal winds.")
    print("An older man with one eye checks you in. The scars on his arms say more than words ever could—this man was once a serious adventurer.")
    print("Around you, chaos reigns: adventuring parties coming and going, some celebrating with laughter, others carrying the wounded—or mourning the fallen.")
    print("“Youngin’!” the man barks. You snap back to attention. “Keep your focus, or you’ll be the one carried out next. So... which biome today?”")

    print("\n🌍 Choose a biome to explore:")
    biome_names = list(biomes.keys())
    for i, biome in enumerate(biome_names, 1):
        req = biomes[biome]["level_required"]
        print(f"{i}. {biome} (Level {req}+) ")
    print(f"{len(biome_names)+1}. Cancel")

    choice = input("Enter the number of your chosen biome: ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(biome_names):
            selected_biome = biome_names[choice - 1]
            required_level = biomes[selected_biome]["level_required"]

            if player.level < required_level:
                print(f"❌ You must be at least Level {required_level} to enter the {selected_biome}.")
                return

            print(f"\n🚪 You enter the {selected_biome}...")
            enemies = biomes[selected_biome]["enemies"]

            while True:
                enemy = random.choice(enemies)
                print(f"\n👹 You encounter a {enemy['name']}!")

                while True:
                    print("What do you want to do?")
                    print("1. Fight")
                    print("2. Run")
                    print("3. View Inventory")
                    action = input("Choose an action: ").strip()

                    if action == "1":
                        combat(enemy, player)

                        if player.hp <= 0:
                            print("💀 You collapse in the wilds... Game over or return to town.")
                            return

                        if player.current_quest and enemy["name"] in player.current_quest["objective"]:
                            player.current_quest["progress"] += 1
                            print(f"📈 Quest progress: {player.current_quest['progress']} / {player.current_quest['goal']}")
                            if player.current_quest["progress"] >= player.current_quest["goal"]:
                                print("\n🎉 Quest complete! Return to the Mercenary Guild to claim your reward.")
                        break

                    elif action == "2":
                        print("\n🏃 You run away!")
                        print("1. Return to Town")
                        print("2. Continue exploring")
                        run_choice = input("Choose an option: ").strip()
                        if run_choice == "1":
                            print("\n🏘️ You return to town.")
                            return
                        elif run_choice == "2":
                            break
                        else:
                            print("❌ Invalid choice.")

                    elif action == "3":
                        print("\n🎒 Inventory:")
                        print(f"Gold: {player.gold}")
                        print(f"HP: {player.hp}")
                        for item, qty in player.inventory.items():
                            print(f"- {item}: {qty}")
                        print("")

                    else:
                        print("❌ Invalid input.")

                print("\nDo you want to:")
                print("1. Continue your journey")
                print("2. Return to town")
                next_action = input("Enter 1 or 2: ").strip()
                if next_action == "2":
                    print("\n🏘️ You return to town.")
                    return

        elif choice == len(biome_names) + 1:
            print("🚪 You step away from the gate.")
        else:
            print("❌ Invalid choice.")
    else:
        print("❌ Invalid input.")
