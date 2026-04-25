
import string

# Load the data from the text file
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Initialize a list to store the scores
all_scores = []

# Process each line in the file
for line in lines:
    # Strip whitespace and newline characters
    line = line.strip()
    # Split the line into components
    parts = line.split(',')

    # Extract scores and convert them to integers
    scores = list(map(int, parts[1:]))  # Skip the name and convert scores to integers
    all_scores.append(scores)

# Calculate the average scores for each class
averages = []
for scores in all_scores:
    average = sum(scores) / len(scores)  # Calculate average
    averages.append(average)

# Print the averages
for idx, avg in enumerate(averages, start=1):
    print(f"Class {idx} average score: {avg:.2f}")
