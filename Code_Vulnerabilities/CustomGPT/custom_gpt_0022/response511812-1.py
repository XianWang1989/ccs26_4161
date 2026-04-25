
import string

# Function to calculate average scores
def calculate_average(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    total_scores = []
    for line in lines:
        new_line = line.strip()  # Remove newline characters
        temp_array = new_line.split(',')  # Split by comma
        scores = list(map(int, temp_array[1:]))  # Convert scores to integers
        total_scores.append(scores)

    # Calculate averages
    averages = [sum(scores) / len(scores) for scores in total_scores]
    return averages

# Example usage
filename = "Class1.txt"
averages = calculate_average(filename)
for i, average in enumerate(averages):
    print(f"Average score for Class {i + 1}: {average:.2f}")
