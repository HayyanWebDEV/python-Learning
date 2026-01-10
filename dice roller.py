import random

# Dice art
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")
}

is_running = True
while is_running:
    dice = []
    total = 0

    numOfDice = int(input("Enter the number of dice: "))

    # Roll dice
    for die in range(numOfDice):
        dice.append(random.randint(1, 6))

    # Print dice art
    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end=" ")
        print()

    # Show total
    total = sum(dice)
    print(f"\nTotal is {total}\n")

    # Ask to play again
    again = input("Roll again? (y/n): ").lower()
    if again != "y" and again != "yes":
        is_running = False

print("Thanks for playing!")
