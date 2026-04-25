
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")

# Using a list to hold all the scores for calculating the average
all_scores = []

# Open the file and process each line
with open("Class1.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        # Strip newline characters and split the line by commas
        tempArray = string.strip(line).split(',')
        # Convert scores to integers and append them to the all_scores list
        scores = [int(score) for score in tempArray[1:]]  # skip the name
        all_scores.extend(scores)

# Calculate and print the average score if requested
if Option == "average score":
    if all_scores:  # Check if there are scores to avoid division by zero
        average = sum(all_scores) / len(all_scores)
        print(f"Average score: {average}")
    else:
        print("No scores available to calculate the average.")
