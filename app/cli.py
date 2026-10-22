"""Local REPL for the family-health harness."""

from agent import turn
from state import STORE, load


def main() -> None:
    house = load()
    print(
        "Family health assistant. Members: Arjun (you), Priya (wife, 34), Aarav (son, 6), Meera (mother, 68).\n"
        "Ctrl-C to exit.\n"
    )
    if house.turns:
        print(f"Resumed {len(house.turns)} turns from {STORE.name}.\n")
    while True:
        try:
            user = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            house.save()
            print()
            break
        if user:
            print(f"Q: {turn(house, user)}\n")
            house.save()


if __name__ == "__main__":
    main()
