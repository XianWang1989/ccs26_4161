
import string

# Function to calculate averages
def calculate_averages(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    scores = []

    for line in lines:
        # Remove newline and split by comma
        parts = line.strip().split(',')
        # Get scores as integers
        student_scores = list(map(int, parts[1:]))  # Skip the name
        scores.append(student_scores)

    return scores

def calculate_average(scores):
    total_scores = []

    for score_list in scores:
        total_scores.append(sum(score_list) / len(score_list))

    return total_scores

# Main execution
filename = "Class1.txt"
scores = calculate_averages(filename)

if "average score" in input("Which order do you want to output? (alphabetical order, highest to lowest, average score) "):
    averages = calculate_average(scores)
    print("Average scores:", averages)
