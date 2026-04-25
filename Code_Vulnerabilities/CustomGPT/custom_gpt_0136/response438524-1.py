
import random

# Function to ask questions and calculate score
def ask_questions():
    score = 0
    questions = {
        "5 + 3": 8,
        "10 - 7": 3,
        "3 * 4": 12,
        "12 / 4": 3,
        "7 + 2": 9,
        "9 - 6": 3,
        "8 * 1": 8,
        "12 / 3": 4,
        "5 + 5": 10,
        "6 * 2": 12
    }

    for question, answer in random.sample(list(questions.items()), 10):
        user_answer = int(input(f"What is {question}? "))
        if user_answer == answer:
            score += 1

    return score

# Save score to file
def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

# Display leaderboard
def display_leaderboard():
    print("\nLeaderboard:")
    with open("leaderboard.txt", "r") as file:
        for line in file:
            print(line.strip())

# Main program
def main():
    name = input("Enter your name: ")
    score = ask_questions()
    save_score(name, score)
    display_leaderboard()

if __name__ == "__main__":
    main()
