import math


def get_coordinates(prompt) -> tuple:
    while True:
        user_input = input(f"{prompt}: ")
        try:
            parts = [p.strip() for p in user_input.split(',')]
            # parts will contain the cord given in input

            if len(parts) != 3:
                print("Invalid syntax")
                continue

            coordenates = []
            # list to contain converted tuple
            for p in parts:
                try:
                    coordenates.append(float(p))
                    # try convert each part of the tuple to float
                except ValueError as e:
                    print(f"Error on parameter '{p}': {e}")
                    raise  # Break out for the other except

            return tuple(coordenates)

        except ValueError:
            # we need this a we use the while True to ask for cord inputs until
            # a valid one is given
            continue


def main():
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    c1 = get_coordinates("Enter new coordinates as floats in format 'x,y,z'")

    x1, y1, z1 = c1
    dist_origin = math.sqrt(x1**2 + y1**2 + z1**2)

    print(f"Got a first tuple: {c1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance to center: {dist_origin:.4f}")

    print("\nGet a second set of coordinates")
    c2 = get_coordinates("Enter new coordinates as floats in format 'x,y,z'")

    x2, y2, z2 = c2
    dist_between = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

    print(f"Distance between the 2 sets of coordinates: {dist_between:.4f}")


if __name__ == "__main__":
    main()
