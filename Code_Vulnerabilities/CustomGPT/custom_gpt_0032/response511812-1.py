
import string

# Define options
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")
choices = ("Class 1", "Class 2", "Class 3")

# Open the file
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Prepare to store results
resultsArray = []
total_scores = []

# Process each line in the file
for line in lines:
    line = line.strip()
    tempArray = line.split(',')
    name = tempArray.pop(0)  # Get the name
    scores = [int(score) for score in tempArray]  # Convert scores to integers
    average = sum(scores) / len(scores)  # Calculate average
    resultsArray.append((name, average))  # Store name and average
    total_scores.append(scores)  # Store the scores for overall average later

# Output result based on selected option
if Option == "average score":
    for entry in resultsArray:
        print(f'{entry[0]}: Average Score = {entry[1]:.2f}')

    overall_average = sum(sum(scores) for scores in total_scores) / sum(len(scores) for scores in total_scores)
    print(f'Overall Average Score = {overall_average:.2f}')
