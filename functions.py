import os
import platform

def validate_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def save_game(file_path, monsters_killed):
    with open(file_path, "a") as file:
        file.write(f"Monsters killed: {monsters_killed}\n")

def load_game(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if "Monsters killed" in line:
                    return int(line.split(":")[1].strip())
    except FileNotFoundError:
        return 0

def print_system_info():
    print(f"Operating System: {os.name}")
    print(f"Python Version: {platform.python_version()}")

def open_treasure_chest(hero_health):
    all_loot = [
        {"name": "Sword of Light", "value": 80},
        {"name": "Healing Potion", "value": 30},
        {"name": "Golden Shield", "value": 60},
        {"name": "Iron Boots", "value": 40},
        {"name": "Magic Ring", "value": 70},
        {"name": "Wooden Stick", "value": 10}
    ]

    if hero_health > 50:
        treasures = [item for item in all_loot if item["value"] > 50]
        print("\n🎉 You opened the treasure chest and found:")
        for item in treasures:
            print(f"- {item['name']} (value: {item['value']})")
    else:
        print("\n🚪 Your health is too low to open the treasure chest. Defeat a monster to unlock it!")
