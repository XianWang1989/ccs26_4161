
import string

# Function to calculate averages
def calculate_averages(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    scores = []

    for line in lines:
        # Strip newline and split the line by commas
        new_line = line.strip().split(',')
        # Extract scores and convert to integers
        scores_list = list(map(int, new_line[1:]))  # Skip the name
        scores.append(scores_list)

    # Calculate averages for each student
    averages = []
    for score in scores:
        avg = sum(score) / len(score)
        averages.append(avg)

    return averages

# Example usage
file_path = "Class1.txt"
average_scores = calculate_averages(file_path)
print("Average Scores:", average_scores)
