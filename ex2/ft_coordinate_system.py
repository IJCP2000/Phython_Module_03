import math


def get_coordinates(prompt) -> tuple:
    while True:
        user_input = input(f"{prompt}: ")
        try:
            # Split by comma and strip whitespace
            parts = [p.strip() for p in user_input.split(',')]

            if len(parts) != 3:
                print("Invalid syntax")
                continue

            # Attempt to convert each part to float
            # If one fails, we catch which one specifically for the error
            coords = []
            for p in parts:
                try:
                    coords.append(float(p))
                except ValueError as e:
                    print(f"Error on parameter '{p}': {e}")
                    raise  # Break out of the inner loop to the outer except

            return tuple(coords)

        except ValueError:
            # This catches the re-raised error from the float conversion
            continue


def main():
    print("=== Game Coordinate System ===")

    # First set of coordinates
    print("\nGet a first set of coordinates")
    c1 = get_coordinates("Enter new coordinates as floats in format 'x,y,z'")

    x1, y1, z1 = c1
    dist_origin = math.sqrt(x1**2 + y1**2 + z1**2)

    print(f"Got a first tuple: {c1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance to center: {dist_origin:.4f}")

    # Second set of coordinates
    print("\nGet a second set of coordinates")
    c2 = get_coordinates("Enter new coordinates as floats in format 'x,y,z'")

    x2, y2, z2 = c2
    # Distance formula: sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)
    dist_between = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

    print(f"Distance between the 2 sets of coordinates: {dist_between:.4f}")


if __name__ == "__main__":
    main()
