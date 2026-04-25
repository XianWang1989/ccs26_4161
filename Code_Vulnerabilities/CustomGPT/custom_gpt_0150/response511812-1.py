
import string

# Read data from the file
file = open("Class1.txt", "r")
lines = file.readlines()

# Initialize list to hold scores
scores = []

# Process each line
for line in lines:
    # Strip newline and split by comma
    tempArray = line.strip().split(',')
    # Extract scores as integers
    resultsArray = [int(score) for score in tempArray[1:]]  # Skip the name
    scores.append(resultsArray)

# Calculate average if needed
average_scores = []
if "average score" in Option:
    for score_list in scores:
        average = sum(score_list) / len(score_list)
        average_scores.append(average)

# Print the averages
for i, avg in enumerate(average_scores):
    print(f"Average score for Class {i + 1}: {avg}")

file.close()
