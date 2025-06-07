# === Mercenary Guild Logic ===

def mercenary_guild(player):
    quests = [
        {
            "name": "Goblin Trouble",
            "description": "Defeat 5 Goblins",
            "objective": "Goblin",
            "progress": 0,
            "goal": 5,
            "reward": {"gold": 50, "item": "Healing Potion"}
        },
        {
            "name": "Skeleton Parade",
            "description": "Defeat 5 Skeletons",
            "objective": "Skeleton",
            "progress": 0,
            "goal": 5,
            "reward": {"gold": 60, "item": "Healing Potion"}
        },
        {
            "name": "Pest Control",
            "description": "Defeat 10 Slimes",
            "objective": "Slime",
            "progress": 0,
            "goal": 10,
            "reward": {"gold": 70, "item": "Healing Potion"}
        },
        {
            "name": "Drain the Swamp",
            "description": "Defeat 10 Killer Wasps and 10 Beetles",
            "objective": "Killer Wasp",  # Note: Only partially implemented
            "progress": 0,
            "goal": 10,
            "reward": {"gold": 100, "item": "Antidote"}
        }
    ]

    print("\n🏰 You enter the Mercenary Guild. The noise hits you like a wave—")
    print("deals being made, stories exaggerated, and business conducted among the realm’s toughest adventurers.")
    print('As you approach the counter, a sharp-eyed elf in a black-and-white uniform greets you.')
    print('"Welcome, Adventurer! We’ve got a few missions that haven’t even hit the board yet—interested?"')
    print("You slide her a gold coin. She winks, nods, and passes you a folded note.")
    print("You carefully unfold it and review the handwritten list:")

    if player.current_quest:
        quest = player.current_quest
        print(f"\n🛡️ Current Quest: {quest['name']}")
        print(f"- {quest['description']}")
        print(f"- Progress: {quest['progress']} / {quest['goal']}")

        if quest["progress"] >= quest["goal"]:
            reward = quest["reward"]
            print(f"\n✅ Objective complete! You turn in the quest and earn {reward['gold']} gold and a {reward['item']}!")
            player.earn_gold(reward["gold"])
            player.add_item(reward["item"])
            player.current_quest = None
    else:
        print("\n📜 Available Quests:")
        for i, quest in enumerate(quests, 1):
            print(f"{i}. {quest['name']} - {quest['description']}")
        print(f"{len(quests)+1}. Cancel")

        choice = input(f"Choose a quest to accept (1–{len(quests)+1}): ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(quests):
                selected = quests[choice - 1]
                player.current_quest = selected.copy()
                print(f"\n✅ You accepted the quest: {selected['name']}")
            elif choice == len(quests) + 1:
                print("🚪 You leave the guild.")
            else:
                print("❌ Invalid choice.")
        else:
            print("❌ Invalid input.")
