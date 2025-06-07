# === Church Healing System ===

def church(player):
    print("\n⛪ You enter the Church and are met with the gentle scent of incense—both invigorating and calming.")
    print("Whispers of prayer float through the air as robed monks attend quietly to the sanctuary.")
    print("A beastman nun approaches, her voice a soft purr: \"Hello, adventurer. Are you here for the priest?\"")
    print("You nod. She guides you past kneeling parishioners to a 7.5-foot tall dragon-kin in white and gold robes.")
    print("He greets you with a toothy smile and eyes your wounds with concern.")
    print("\"One prayer can heal you right up,\" he says warmly, before clearing his throat and gesturing to the offering plate beside him, with his tail.")

    cost = 15
    max_hp = 100 + player.level * 5
    print(f"\n💰 Offering required: {cost} gold (You currently have {player.gold} gold)")
    choice = input("Do you place an offering for healing? (yes/no): ").strip().lower()

    if choice in ["yes", "y"]:
        if player.spend_gold(cost):
            player.hp = max_hp
            print("✨ A soft glow surrounds you as divine warmth restores your body. Your HP is fully restored.")
        else:
            print("❌ You fumble through your pouch but don’t have enough gold. The priest gently nods in understanding.")
    else:
        print("🙏 You bow in thanks and respectfully decline the priest’s offer before exiting the sanctuary.")
