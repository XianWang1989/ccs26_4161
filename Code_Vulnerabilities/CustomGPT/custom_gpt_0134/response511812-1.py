
import string

def calculate_average(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    all_scores = []
    for line in lines:
        # Split the line and convert scores to integers
        parts = line.strip().split(',')
        scores = list(map(int, parts[1:]))  # Convert scores to integers
        all_scores.append(scores)

    return all_scores

def average_scores(scores):
    averages = []
    for score_list in scores:
        avg = sum(score_list) / len(score_list) if score_list else 0
        averages.append(avg)
    return averages

# User input
option = input("Which output do you want? (alphabetical order, highest to lowest, average score): ")

# Process the file and get scores
file_path = "Class1.txt"
scores = calculate_average(file_path)

if option == "average score":
    averages = average_scores(scores)
    for idx, avg in enumerate(averages):
        print(f"Class {idx + 1} Average Score: {avg:.2f}")
