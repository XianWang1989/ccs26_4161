
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options))  # Use input() for Python 3
choices = ("Class 1", "Class 2", "Class 3")

with open("Class1.txt", "r") as file:
    lines = file.readlines()

resultsArray = []

# Process each line in the file
for line in lines:
    new_line = line.strip()  # Remove trailing newline characters
    tempArray = new_line.split(',')  # Split the line on commas
    name = tempArray.pop(0)  # Remove and save the name
    scores = [int(score) for score in tempArray]  # Convert scores to integers
    resultsArray.append(scores)  # Append scores to results array

if Option == "average score":
    total_scores = [0] * len(resultsArray[0])  # Initialize total scores list
    for scores in resultsArray:
        for i, score in enumerate(scores):
            total_scores[i] += score  # Accumulate scores

    averages = [total / len(resultsArray) for total in total_scores]  # Calculate averages
    print("Average scores:", averages)  # Output the averages
