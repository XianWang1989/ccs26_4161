
import random

def ask_math_questions():
    score = 0
    for _ in range(10):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2
        user_answer = int(input(f"What is {num1} + {num2}? "))
        if user_answer == correct_answer:
            score += 1
    return score

def save_score_to_file(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

def read_leaderboard():
    print("\nLeaderboard:")
    try:
        with open("leaderboard.txt", "r") as file:
            for line in file:
                print(line, end="")  # end="" avoids double new lines
    except FileNotFoundError:
        print("No scores yet!")

def main():
    name = input("Enter your name: ")
    score = ask_math_questions()
    print(f"Your score: {score} out of 10")

    save_score_to_file(name, score)
    read_leaderboard()

if __name__ == "__main__":
    main()
