
import string

# Function to calculate averages from the file
def calculate_averages(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    results = []

    for line in lines:
        # Remove newline and split the line by commas
        line = line.strip()
        temp_array = line.split(',')

        # Get the scores as integers
        scores = list(map(int, temp_array[1:]))  # Ignore name and convert scores to int
        results.append(scores)

    return results

# Calculate average scores
def calculate_average(scores_list):
    if not scores_list:
        return 0
    total_scores = [sum(scores) for scores in scores_list]
    average = sum(total_scores) / len(total_scores)
    return average

# Main execution
filename = "Class1.txt"
scores_list = calculate_averages(filename)
average = calculate_average(scores_list)

print(f"The average score is: {average}")
