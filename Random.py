import random
from idlelib.pyshell import extended_linecache_checkcache

print("This is a no. guessing game")

lowest_num = int(input("Enter a number for lower range: "))
highest_num = int(input("Enter a number for higher range: "))
print(f"This is the lowest number: {lowest_num} and highest number: {highest_num}")
is_running = True
answer = random.randint(lowest_num, highest_num)
guesses = 0

while is_running:

    guess = input("Enter a number: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("You guessed out of range. Try again")
            print(f"This is the lowest number: {lowest_num} and highest number: {highest_num}")
            print(f"please select within the range!")
        elif guess < answer:
            print("You have guessed too low. Try again")
        elif guess > answer:
            print("You have guessed too high. Try again")
        else:
            print("You have guessed correctly")
            print(f"you have guessed in {guesses} guesses")
            is_running = False

    else:
        print("invalid guess!")
        print(f"please enter a number within the range of {lowest_num} and {highest_num}")
