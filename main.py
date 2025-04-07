from hero import Hero
from monster import Monster
from functions import validate_input, save_game, load_game, print_system_info, open_treasure_chest

def main():
    print_system_info()

    hero = Hero()
    monster = Monster()

    print(f"Hero stats - Combat Strength: {hero.combat_strength}, Health Points: {hero.health_points}")
    print(f"Monster stats - Combat Strength: {monster.combat_strength}, Health Points: {monster.health_points}")

    monsters_killed = load_game("save.txt")

    while hero.health_points > 0 and monster.health_points > 0:
        hero_damage = hero.hero_attacks()
        monster.health_points -= hero_damage
        print(f"Hero attacks! Monster takes {hero_damage} damage. Monster HP: {monster.health_points}")

        if monster.health_points <= 0:
            print("Monster defeated!")
            monsters_killed += 1
            break

        monster_damage = monster.monster_attacks()
        hero.health_points -= monster_damage
        print(f"Monster attacks! Hero takes {monster_damage} damage. Hero HP: {hero.health_points}")

        if hero.health_points <= 0:
            print("Hero is defeated!")

    save_game("save.txt", monsters_killed)
    print(f"Total monsters killed: {monsters_killed}")

    # Treasure chest feature
    open_treasure_chest(hero.health_points)

if __name__ == "__main__":
    main()
