import random

def combat(monster, player):
    print(f"\n⚔️ You engage in combat with a {monster['name']}!")
    monster_hp = monster["hp"]

    while monster_hp > 0 and player.hp > 0:
        # Player's turn
        damage = random.randint(8, 15)
        monster_hp -= damage
        print(f"🗡️ You hit the {monster['name']} for {damage} damage!")

        if monster_hp <= 0:
            print(f"💀 The {monster['name']} has been defeated!")
            break

        # Monster's turn
        enemy_damage = random.randint(monster["attack_min"], monster["attack_max"])
        player.hp -= enemy_damage
        print(f"👹 The {monster['name']} hits you for {enemy_damage} damage! (Your HP: {player.hp})")

        if player.hp <= 0:
            print("☠️ You have been defeated!")
            return

    # Loot
    for item, (min_qty, max_qty) in monster["drops"].items():
        qty = random.randint(min_qty, max_qty)
        player.add_item(item, qty)
        print(f"🎁 You received: {qty} x {item}")

    gold_earned = random.randint(*monster["gold"])
    player.earn_gold(gold_earned)
    print(f"💰 You looted {gold_earned} gold!")

    if "exp" in monster:
        player.gain_exp(monster["exp"])
