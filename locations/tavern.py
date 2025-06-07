import random

def tavern(player=None):  # You can optionally pass in a player for future expansion (e.g. events)
    intro = (
        "🍻 You enter the Tavern. The fire crackles and a bard sings off-key, recounting tales of legendary adventurers.\n"
        "You seat yourself within earshot of chatting parties and order your meal.\n"
        "As you sip and chew, you begin to overhear whispers around the room..."
    )

    rumors = [
        "“Did you hear? The young elf girl at the Mercenary Guild has secret missions,” one whispers. “Yeah, but I heard you’ll have to pay—anything less than 1 gold and she’ll send you into the wilds for weeks.”",
        "“I wonder what exactly they’re crafting that requires so many monster drops?” a young human whispers to his party. “That’s none of my concern,” replies an older elf woman, sipping her drink. “As long as the Crafting Hall is secretly buying, I’ll happily sell.”",
        "“It’s not worth it!” a drunk barbarian complains. “Of course it is,” replies a mage. “The Church’s healing is as strong as an Ultimate Healing Potion—and way cheaper.”",
        "A loud beastman enters, slamming a bag of gold on the counter. “Drinks on me! I’ve struck it rich!” Nearby whispers speculate: “E-chel’n just hit the Arctic Biome. Probably sold a Dragon Force Pill.” “Lucky bastard,” a human snorts.",
        "A party enters. “I can’t believe you finally learned Fireball!” an old mage laughs. “Who would’ve thought a monster would drop it?” The young barbarian grins. “Forest Biome’s wild, man.”"
    ]

    closing = "You take all this in as you eat, drink, and rest."

    print(f"\n{intro}\n\n💬 {random.choice(rumors)}\n\n{closing}")

