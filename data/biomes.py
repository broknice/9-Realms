             # === Biome Definitions ===

biomes = {
                 "Forest": {
                     "level_required": 1,
                     "enemies": [
                         {"name": "Goblin", "hp": 25, "attack_type": "Slash", "attack_min": 4, "attack_max": 7, "drops": {"Goblin Ear": (1, 2)}, "gold": (5, 10), "exp": 40},
                         {"name": "Night Wolf", "hp": 30, "attack_type": "Bite", "attack_min": 5, "attack_max": 9, "drops": {"Wolf Fang": (1, 1)}, "gold": (6, 12), "exp": 50},
                         {"name": "Poison Flower", "hp": 10, "attack_type": "Spit", "attack_min": 3, "attack_max": 5, "drops": {"Mystic Flower": (1, 1)}, "gold": (4, 8), "exp": 30},
                         {"name": "Warlock", "hp": 35, "attack_type": "Fireball", "attack_min": 6, "attack_max": 10, "drops": {"Spellbook: Fireball": (1, 1)}, "gold": (10, 15), "exp": 60}
                     ]
                 },
                 "Swamp": {
                     "level_required": 2,
                     "enemies": [
                         {"name": "Slime", "hp": 20, "attack_type": "Splatter", "attack_min": 2, "attack_max": 4, "drops": {"Slime Gel": (1, 2)}, "gold": (3, 6), "exp": 25},
                         {"name": "Beetle", "hp": 15, "attack_type": "Bite", "attack_min": 2, "attack_max": 5, "drops": {"Antenna": (1, 1)}, "gold": (2, 4), "exp": 20},
                         {"name": "Killer Wasp", "hp": 10, "attack_type": "Sting", "attack_min": 3, "attack_max": 6, "drops": {"Wasp Stinger": (1, 2)}, "gold": (4, 7), "exp": 35}
                     ]
                 },
                 "Cave": {
                     "level_required": 3,
                     "enemies": [
                         {"name": "Bat", "hp": 25, "attack_type": "Bite", "attack_min": 3, "attack_max": 6, "drops": {"Bat Wing": (1, 2)}, "gold": (2, 5), "exp": 25},
                         {"name": "Skeleton", "hp": 25, "attack_type": "Bash", "attack_min": 4, "attack_max": 8, "drops": {"Bone": (1, 2)}, "gold": (6, 10), "exp": 55},
                         {"name": "Scorpion", "hp": 20, "attack_type": "Sting", "attack_min": 5, "attack_max": 9, "drops": {"Exoskeleton": (1, 1)}, "gold": (5, 8), "exp": 45},
                         {"name": "Lightning Rat", "hp": 20, "attack_type": "Shock", "attack_min": 5, "attack_max": 10, "drops": {"Lightning Ball": (1, 1)}, "gold": (7, 12), "exp": 50},
                         {"name": "Witch", "hp": 30, "attack_type": "Curse", "attack_min": 6, "attack_max": 11, "drops": {"Wizard Staff": (1, 1)}, "gold": (10, 15), "exp": 70}
                     ]
                 },
                 "Arctic": {
                     "level_required": 7,
                     "enemies": [
                         {"name": "Phantom", "hp": 50, "attack_type": "Screech", "attack_min": 6, "attack_max": 12, "drops": {"Ectoplasm": (1, 1)}, "gold": (10, 15), "exp": 70},
                         {"name": "Ogre", "hp": 45, "attack_type": "Bash", "attack_min": 7, "attack_max": 13, "drops": {"Enchanted Club": (1, 1)}, "gold": (12, 18), "exp": 90},
                         {"name": "Werewolf", "hp": 40, "attack_type": "Slash", "attack_min": 8, "attack_max": 14, "drops": {"Werewolf Hide": (1, 1)}, "gold": (15, 20), "exp": 100},
                         {"name": "Dragon", "hp": 80, "attack_type": "Fire Blast", "attack_min": 10, "attack_max": 20, "drops": {"Dragon Core": (1, 1)}, "gold": (25, 40), "exp": 200}
                     ]
                 }
             }
