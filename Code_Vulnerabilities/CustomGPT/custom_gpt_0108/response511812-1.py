
import string

# Function to calculate average scores
def calculate_average(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    scores = []
    for line in lines:
        # Strip whitespace and split by commas
        parts = line.strip().split(',')
        # Convert score strings to integers and append to scores
        scores.append(list(map(int, parts[1:])))  # Skip the name

    # Calculate averages for each student
    averages = [sum(score) / len(score) for score in scores]
    return averages

# Path to the file
file_path = "Class1.txt"
averages = calculate_average(file_path)

# Print the results
for avg in averages:
    print(f"Average score: {avg:.2f}")
