def use_item(player, item_name):
    if item_name == "Healing Potion":
        if player.remove_item(item_name):
            heal_amount = 50
            player.hp += heal_amount
            max_hp = 100 + player.level * 5
            if player.hp > max_hp:
                player.hp = max_hp
            print(f"🧪 You used a Healing Potion and restored {heal_amount} HP. (Current HP: {player.hp})")
        else:
            print("❌ You don't have any Healing Potions.")

    elif item_name.startswith("Spellbook: "):
        spell_name = item_name.split(": ")[1]
        if spell_name in player.spells_learned:
            print(f"📚 You already know the {spell_name} spell.")
        else:
            if player.remove_item(item_name):
                player.spells_learned.append(spell_name)
                print(f"✨ You learned the spell: {spell_name}!")
            else:
                print(f"❌ You don't have a {item_name}.")

    else:
        print(f"❓ {item_name} can't be used right now.")
