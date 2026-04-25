
import string

# Options for output order
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")

# Open the file and read the lines
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Initialize variables
scores = []

# Process each line
for line in lines:
    # Remove newline and split by commas
    new_line = line.strip()
    tempArray = new_line.split(',')

    # Extract name and scores, and convert scores to integers
    name = tempArray[0]
    scores_list = list(map(int, tempArray[1:]))

    # Append the scores to the main list
    scores.append(scores_list)

# Calculate the average if the option is selected
if Option == "average score":
    total_scores = [0] * len(scores[0])  # Initialize a list to hold the sums

    # Sum the scores column-wise
    for score_set in scores:
        for i in range(len(score_set)):
            total_scores[i] += score_set[i]

    # Calculate averages
    average_scores = [total / len(scores) for total in total_scores]

    # Print the average scores
    print("Average scores:", average_scores)
