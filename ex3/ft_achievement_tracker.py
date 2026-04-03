import random
# from pprint import pprint


def get_player_achievements(player: set) -> set:
    achievements = {
                   'Crafting Genius', 'Strategist', 'World Savior',
                   'Speed Runner', 'Survivor',
                   'Master Explorer', 'Treasure Hunter', 'Unstoppable',
                   'First Steps', 'Collector Supreme', 'Untouchable',
                   'Sharp Mind', 'Boss Slayer'
                  }

    x = random.randrange(1, len(achievements) + 1)

    return set(random.sample(list(achievements), x))


def main():
    all_achievements = {
                        'Crafting Genius', 'Strategist', 'World Savior',
                        'Speed Runner', 'Survivor',
                        'Master Explorer', 'Treasure Hunter', 'Unstoppable',
                        'First Steps', 'Collector Supreme', 'Untouchable',
                        'Sharp Mind', 'Boss Slayer'
                      }

    player_data = {
                "Alice": set(), "Bob": set(),
                "Charlie": set(), "Dylan": set()
              }

    earned_achieve = set()
    common_achieve = None
    unique_to_player = set()
    missing_achieves = set()

    print("=== Achievement Tracker System ===")

    for name in player_data:

        achievements = get_player_achievements(name)
        player_data[name] = achievements

        earned_achieve = earned_achieve.union(achievements)

        if common_achieve is None:
            common_achieve = achievements.copy()
        else:
            common_achieve = common_achieve.intersection(achievements)

        print(f"\nPlayer {name}: {player_data[name]}")

    print(f"\nAll distinct achievements: {earned_achieve}")
    print(f"\nCommon achievements: {common_achieve}")

    print()

    for name, achieves in player_data.items():
        unique_to_player = achieves.copy()

        for other_name, other_achieves in player_data.items():
            if name != other_name:
                unique_to_player.difference_update(other_achieves)

        print(f"Only {name} has: {unique_to_player}")

    print()

    for name, achieves in player_data.items():
        missing_achieves = all_achievements.difference(achieves)

        print(f"{name} is missing: {missing_achieves}")


if __name__ == "__main__":
    main()
