import sys


def input_given() -> dict:

    inventory = {}
    # empty dicionary

    args = sys.argv[1:]
    # skips the program name and only the arguments are "stored"

    if not args:
        print("No item and/or quantity given")
        sys.exit(1)

    for param in args:
        parts = param.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter {param}")
            continue

        item, quantity_str = parts

        if item in inventory:
            print(f"Redundant item {item} - discarding")
            continue

        try:
            quantity = int(quantity_str)
            inventory[item] = quantity
            # So it stores as corespondent key-value pair
        except ValueError as e:
            print(f"Quantity error for {item}: {e}")
            continue

    return inventory


def main():
    print("=== Inventory System Analysis ===")

    inventory = input_given()

    if not inventory:
        print("Nothing was given/ No allowed data was given")
        return

    print(f"Got inventory: {inventory}")

    items = list(inventory.keys())
    print(f"Item list: {items}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total_quantity}")

    for item, quantity in inventory.items():
        percentage = (quantity / total_quantity) * 100
        print(f"Item {item} represents {percentage:.1f}%")

    most = max(inventory.values())
    least = min(inventory.values())

    check_max = 0
    check_min = 0

    for item, quantity in inventory.items():

        if quantity == most and check_max == 0:
            print(f"Item most abundant:"
                  f" {item} with quantity {most}")
            check_max += 1
        if quantity == least and check_min == 0:
            print(f"Item least abundant:"
                  f" {item} with quantity {least}")
            check_min += 1

    inventory.update({"magic_item": 1})
    print(inventory)


if __name__ == "__main__":
    main()
