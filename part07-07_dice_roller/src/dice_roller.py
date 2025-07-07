import random

def roll(die: str, dice: dict) -> int:
    """Rolls the specified die and returns a random side."""
    return random.choice(dice[die])

def play(die1: str, die2: str, times: int, dice: dict) -> tuple:
    """Simulates a game between two dice."""
    die1_wins = 0
    die2_wins = 0
    ties = 0

    for _ in range(times):
        roll1 = roll(die1, dice)
        roll2 = roll(die2, dice)

        if roll1 > roll2:
            die1_wins += 1
        elif roll1 < roll2:
            die2_wins += 1
        else:
            ties += 1

    return (die1_wins, die2_wins, ties)

if __name__ == "__main__":
    # Define DICE inside the main block
    DICE = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4],
    }

    # Test roll function
    print("Die A rolls: ", end="")
    for i in range(20):
        print(roll("A", DICE), end=" ")
    print()

    print("Die B rolls: ", end="")
    for i in range(20):
        print(roll("B", DICE), end=" ")
    print()

    print("Die C rolls: ", end="")
    for i in range(20):
        print(roll("C", DICE), end=" ")
    print()

    # Test play function
    result = play("A", "C", 1000, DICE)
    print(f"Result of Die A vs Die C: {result}")

    result = play("B", "B", 1000, DICE)
    print(f"Result of Die B vs Die B: {result}")
