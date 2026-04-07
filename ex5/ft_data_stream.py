import random
from typing import Generator, Tuple


# endless generator func

def gen_event() -> Generator[Tuple[str, str], None, None]:
    names = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "move", "climb", "grab", "use",
               "eat", "sleep", "swim", "release"]

    # The loop make it possible to use func infinetely
    while True:
        name = random.choice(names)
        action = random.choice(actions)
        yield (name, action)


def consume_event(ten_loops: list) -> list:
    target = random.choice(ten_loops)
    print(f"Got event from list: {target}")
    ten_loops.remove(target)
    return ten_loops
    # Lists are mutable, I did not need to return, the og
    # list would update automatically


def main():
    print("=== Game Data Stream Processor ===")

    i = 0
    generator = gen_event()
    for _ in range(1000):
        name, action = next(generator)
        print(f"Event {i}: Player {name} did action {action}")
        i += 1

    ten_loops = []
    for _ in range(10):
        lists = next(generator)
        # To be able to get the Tuple (name, action)
        ten_loops.append(lists)
        # save the tuple to the list

    print(f"Built list of 10 events: {ten_loops}")

    for _ in range(10):
        consume_event(ten_loops)
        print(f"Remains in list: {ten_loops}")


if __name__ == "__main__":
    main()
