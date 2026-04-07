import random


def main():
    print("=== Game Data Alchemist ===")

    names = ["Alice", "bob", "Charlie", "dylan",
             "Emma", " Gregory", "john", "kevin",
             "Liam"]

    print(f"\nInitial list of players:"
          f" {names}")

    capital_names = {name.capitalize() for name in names}
    print(f"New list with all names capitalized:"
          f" {capital_names}")

    only_capital_og = {name: len(name) for name in names if name[0].isupper()}
    print(f"New list of capitalized names only:"
          f" {only_capital_og}")

    scores = {name: random.randint(50, 1000) for name in capital_names}
    print(f"\nScore dict: {scores}")

    all_scores = scores.values()
    avrg_scores = sum(all_scores) / len(all_scores)
    print(f"Score average is {avrg_scores:.2f}")

    hight_scores = {name: score for name,
                    score in scores.items() if score > 700}
    print(f"High scores: {hight_scores}")


if __name__ == "__main__":
    main()
