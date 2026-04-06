import sys


def input_given() -> set:

    inventory = set()
    # creating an empyt set

    args = sys.argv[1:]
    # skips the program name and only the arguments are "stored"

    if not args:
        print("No item and/or quantity given")
        sys.exit()

    for param in args:
        parts = param.split(":")

        if len(parts) != 2:
            raise Exception

        item, quantity = parts

        try:
            if inventory.values(item) == "True":
                print(f"Redundant item {item} - discarding")
                
            int(quantity)
            inventory.update(parts)
        except ValueError as e:
            print(f"Quantity error for {item}: {e}")
            continue
        except Exception:
            print(f"Error - invalid parameter {parts}")
            continue

    return inventory()


def main(inventory_items):
    inventory = set()

    print("=== Inventory System Analysis ===")

    inventory = input_given(inventory_items)

    print(f"Got inventory: {inventory}")

    items = inventory.keys()
    print(f"Item list: {items}")

    print(f"Total quantity of the {len(items)} items: ")

