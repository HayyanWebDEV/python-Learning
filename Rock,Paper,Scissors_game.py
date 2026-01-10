import random

options = ["rock", "paper", "scissors"]
running = True

while running:
    player_choice = None
    computer_choice = random.choice(options)


    while player_choice not in options:
        player_choice = input("Player chooses rock, paper, or scissors: ").lower()

    print(f"Computer chose: {computer_choice}")
    print(f"Player chose: {player_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("wanna play again? (y/n)").lower()
    if play_again != "y" and play_again != "yes":
        running = False

print("Thank you for playing!")
