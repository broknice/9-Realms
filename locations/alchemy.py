def alchemy_shop(player):
    print("\n🧪 You enter the Alchemy Shop and are immediately greeted by a young assistant.")
    print("His badge—a furnace with a single star—marks him as a 1-star alchemist in training.")
    print("Brimming with enthusiasm, he launches into an animated explanation of the shop’s newest items and mixtures.")
    print("You clear your throat. He blinks, straightens up, and collects himself.")
    print('"Ah! Right—welcome, honored customer. What would you like to do today?"')

    def sell_items(player, shop_items):
        print(f"\n💰 You have {player.gold} gold.")
        sell_prices = {item: price for item, price in shop_items.items() if item in player.inventory}

        if not sell_prices:
            print("You have no items to sell.")
            return

        print("Sellable items:")
        for i, (item, price) in enumerate(sell_prices.items(), 1):
            qty = player.inventory[item]
            print(f"{i}. {item} (You have {qty}) - {price // 2} gold each")
        print(f"{len(sell_prices)+1}. Cancel")

        choice = input("Enter the number of the item you want to sell: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(sell_prices):
                item_name = list(sell_prices.keys())[choice - 1]
                max_qty = player.inventory[item_name]
                amount = input(f"How many {item_name}s would you like to sell? (Max {max_qty}): ")
                if amount.isdigit():
                    amount = int(amount)
                    if 0 < amount <= max_qty:
                        total = (shop_items[item_name] // 2) * amount
                        player.gold += total
                        player.remove_item(item_name, amount)
                        print(f"✅ Sold {amount} x {item_name} for {total} gold.")
                    else:
                        print("❌ Invalid quantity.")
            elif choice == len(sell_prices) + 1:
                return
            else:
                print("❌ Invalid selection.")

    def trade_items(player, shop_items):
        print(f"\n🔁 Trade Mode: You have {player.gold} gold and the following items:")
        tradeables = {item: price for item, price in shop_items.items() if item in player.inventory}

        if not tradeables:
            print("You have no tradeable items.")
            return

        for item, price in tradeables.items():
            print(f"- {item}: {player.inventory[item]} (Value: {price} gold each)")

        trade_from = input("Enter the name of the item you want to trade: ").strip()
        if trade_from not in tradeables:
            print("❌ You don't have that item to trade.")
            return

        max_qty = player.inventory[trade_from]
        qty = input(f"How many {trade_from}s would you like to trade? (Max {max_qty}): ")
        if not qty.isdigit() or int(qty) < 1 or int(qty) > max_qty:
            print("❌ Invalid quantity.")
            return
        qty = int(qty)
        trade_value = shop_items[trade_from] * qty

        print(f"\nAvailable items to receive (Total trade value: {trade_value} gold):")
        for i, (item, price) in enumerate(shop_items.items(), 1):
            tradeable_qty = trade_value // price
            if tradeable_qty > 0:
                print(f"{i}. {item} - {price} gold (You can receive up to {tradeable_qty})")
        print(f"{len(shop_items)+1}. Cancel")

        choice = input("Enter the number of the item you want in return: ")
        if not choice.isdigit():
            print("❌ Invalid choice.")
            return
        choice = int(choice)
        if 1 <= choice <= len(shop_items):
            receive_item = list(shop_items.keys())[choice - 1]
            price = shop_items[receive_item]
            max_receive = trade_value // price
            qty_receive = input(f"How many {receive_item}s would you like? (Max {max_receive}): ")
            if qty_receive.isdigit():
                qty_receive = int(qty_receive)
                if 1 <= qty_receive <= max_receive:
                    player.remove_item(trade_from, qty)
                    player.add_item(receive_item, qty_receive)
                    leftover = trade_value - (qty_receive * price)
                    player.gold += leftover
                    print(f"✅ Traded {qty} x {trade_from} for {qty_receive} x {receive_item} and received {leftover} gold in change.")
                else:
                    print("❌ Invalid quantity.")
        elif choice == len(shop_items) + 1:
            return
        else:
            print("❌ Invalid selection.")

    # Define shop inventory
    shop_items = {
        "Healing Potion": 25,
        "Toxin Vial": 50,
        "Ultimate Healing Potion": 100,
        "Antidote": 20,
        "Alchemist’s Fire": 60,
        "Bonemeal": 100,
        "Wolf Armor": 150,
        "Mystic Enhancement Potion": 200,
        "Dragon Force Pill": 350
    }

    while True:
        print("\nWhat would you like to do?")
        print("1. Buy Items")
        print("2. Sell Items")
        print("3. Trade Items")
        print("E. Exit Shop")

        choice = input("Choose an option: ").strip().lower()

        if choice == 'e':
            print("\n👋 Leaving the Alchemy Shop.")
            break

        elif choice == "1":
            print(f"\n🛒 Items for Sale (You have {player.gold} gold):")
            for i, (item, price) in enumerate(shop_items.items(), 1):
                print(f"{i}. {item} - {price} gold")
            print(f"{len(shop_items)+1}. Cancel")

            choice = input("Enter the number of the item you want to buy: ")

            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(shop_items):
                    item_name = list(shop_items.keys())[choice - 1]
                    item_price = shop_items[item_name]

                    if player.gold >= item_price:
                        player.gold -= item_price
                        player.inventory[item_name] = player.inventory.get(item_name, 0) + 1
                        print(f"✅ You bought 1 x {item_name} for {item_price} gold.")
                    else:
                        print("❌ Not enough gold.")
                elif choice == len(shop_items) + 1:
                    continue
                else:
                    print("❌ Invalid selection.")

        elif choice == "2":
            sell_items(player, shop_items)

        elif choice == "3":
            trade_items(player, shop_items)

        else:
            print("❌ Invalid input.")
