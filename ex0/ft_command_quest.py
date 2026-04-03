import sys


def main() -> None:

    args = sys.argv[1:]
    numb_args = len(args)

    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if numb_args == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {numb_args}")

    i = 1
    while i <= numb_args:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1

    print(f"Total arguments: {numb_args + 1}")


if __name__ == "__main__":
    main()
