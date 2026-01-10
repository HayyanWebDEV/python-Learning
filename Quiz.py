Questions = (
    "What is the capital of Canada?",
    "Which planet is known as the Red Planet?",
    "Who painted the famous artwork Mona Lisa?",
    "Which is the largest ocean on Earth?",
    "In computing, what does 'CPU' stand for?"
)

options = (
    ("A. Toronto", "B. Vancouver", "C. Ottawa", "D. Montreal"),
    ("A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"),
    ("A. Pablo Picasso", "B. Vincent van Gogh", "C. Leonardo da Vinci", "D. Michelangelo"),
    ("A. Indian Ocean", "B. Pacific Ocean", "C. Atlantic Ocean", "D. Arctic Ocean"),
    ("A. Central Processing Unit", "B. Computer Power Unit", "C. Central Programming Utility", "D. Control Processing Unit")
)

Answers = ("C", "B", "C", "B", "A")

score = 0
Guesses = []
question_num = 0

for question in Questions:
    print("-------------------------")
    print(question_num + 1, question)
    print()

    for option in options[question_num]:
        print(option)

    print("____")
    guess = input("Enter A,B,C,D: ").upper()

    if guess in ("A", "B", "C", "D"):
        if guess == Answers[question_num]:
            score += 1
            print(" Correct!")
        else:
            print(" Incorrect! The correct answer was", Answers[question_num])
    else:
        print("Invalid Input!")

    question_num += 1

final_Score = score / len(Questions) * 100
print("\n=========================")
print(f"Your final score:{final_Score}%")
print("=========================")
