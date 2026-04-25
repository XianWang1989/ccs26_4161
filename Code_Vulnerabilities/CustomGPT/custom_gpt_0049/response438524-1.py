
import random

def ask_questions():
    score = 0
    questions = {
        "What is 2 + 2?": 4,
        "What is 5 * 3?": 15,
        "What is 12 / 4?": 3,
        "What is 9 - 5?": 4,
        "What is 7 + 3?": 10,
        "What is 8 - 2?": 6,
        "What is 6 * 2?": 12,
        "What is 10 / 2?": 5,
        "What is 15 - 10?": 5,
        "What is 3 + 6?": 9
    }

    for question, answer in random.sample(list(questions.items()), 10):
        user_answer = int(input(question + " "))
        if user_answer == answer:
            score += 1
    return score

def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No leaderboard exists yet.")

def main():
    name = input("Enter your name: ")
    score = ask_questions()
    save_score(name, score)
    print("Score saved!")
    print("Current leaderboard:")
    display_leaderboard()

if __name__ == "__main__":
    main()
