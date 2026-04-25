
import random

def ask_math_questions():
    score = 0
    for _ in range(10):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        correct_answer = a + b
        answer = input(f"What is {a} + {b}? ")
        if answer.isdigit() and int(answer) == correct_answer:
            score += 1
    return score

def save_score_to_file(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            print("\nLeaderboard:")
            for line in file:
                print(line, end="")  # 'end=""' prevents adding extra newline
    except FileNotFoundError:
        print("No scores recorded yet.")

def main():
    name = input("Enter your name: ")
    score = ask_math_questions()
    print(f"{name}, your score is: {score} out of 10")
    save_score_to_file(name, score)
    display_leaderboard()

if __name__ == "__main__":
    main()
