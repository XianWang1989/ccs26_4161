# Function to save the score
def save_score(name, score):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}: {score} out of 10\n")

# Function to display leaderboard
def show_leaderboard():
    print("Leaderboard:")
    with open("leaderboard.txt", "r") as file:
        for line in file:
            print(line.strip())
