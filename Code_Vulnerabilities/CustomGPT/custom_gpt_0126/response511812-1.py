
import string

# Read data from the file
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Store scores for each student
resultsArray = []

# Process each line in the file
for line in lines:
    new_line = line.strip()  # Remove newlines and extra spaces
    tempArray = new_line.split(',')

    # Extract the scores and convert them to integers
    scores = list(map(int, tempArray[1:]))  # Skip the name and convert scores to int
    resultsArray.append(scores)

# Define a function to calculate average
def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0

# Calculate averages for each student
averages = [calculate_average(scores) for scores in resultsArray]

# Print the averages
for idx, avg in enumerate(averages, start=1):
    print(f"Average score for Class {idx}: {avg:.2f}")
