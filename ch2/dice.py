"""Simulate rolling a six-sided dice"""

import random

DICE_MIN = 1
DICE_MAX = 6

def main() -> None:

    """Simulates rolling a six-sided dice five times and prints the results."""
    for i in range(5):
        dice1 = random.randint(DICE_MIN, DICE_MAX)
        dice2 = random.randint(DICE_MIN, DICE_MAX)
        print(f"Roll {i + 1}: Dice 1: {dice1}, Dice 2: {dice2}")

if __name__ == "__main__":
    main()
