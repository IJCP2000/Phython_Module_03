import sys


def errors(args: str) -> bool:
    try:
        int(args)
        return True
    except ValueError:
        return False


def main() -> None:

    args = sys.argv[1:]
    # skips program name
    scores = []
    # list to store & organize valid inpts

    print("=== Player Score Analytics ===")

    for arg in args:
        if errors(arg):
            scores.append(int(arg))
        else:
            print(f"Invalid parameter: {arg}")

    if len(scores) > 0:
        print(f"Scores processed: {scores}")
        print(f"Total Players: {len(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    else:
        print("No scores provided. Usage: python3"
              " ft_score_analytics.py <score1> <score2> ...")
        sys.exit(1)


if __name__ == "__main__":
    main()
