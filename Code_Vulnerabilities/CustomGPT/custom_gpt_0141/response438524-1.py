
import random

# Function to simulate asking math questions
def ask_math_questions():
    score = 0
    for _ in range(10):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 + num2  # Example of a math question
        user_answer = int(input(f"What is {num1} + {num2}? "))
        if user_answer == answer:
            score += 1
    return score

# Function to save scores to the leaderboard file
def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

# Function to read and display previous scores
def display_leaderboard():
    print("\nLeaderboard:")
    try:
        with open("leaderboard.txt", "r") as file:
            for line in file:
                print(line.strip())  # Display each line without extra spaces
    except FileNotFoundError:
        print("No leaderboard found yet.")

# Main program
def main():
    name = input("Enter your name: ")
    score = ask_math_questions()
    print(f"Your score: {score} out of 10")

    # Save score to file
    save_score(name, score)

    # Display the leaderboard
    display_leaderboard()

if __name__ == "__main__":
    main()
