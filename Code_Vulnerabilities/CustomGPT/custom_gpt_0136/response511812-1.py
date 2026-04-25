
import string

# Get the option from the user
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")
file = open("Class1.txt", "r")

# Initialize list for scores
scores = []

# Read lines from the file
lines = file.readlines()
for line in lines:
    new_line = line.strip()
    tempArray = new_line.split(',')

    # Extract scores and convert to integers
    scores_list = list(map(int, tempArray[1:]))  # Convert scores to integers
    scores.append(scores_list)

# Calculate the average if the chosen option is 'average score'
if Option == "average score":
    # Flatten the list of scores and calculate average
    all_scores = [score for sublist in scores for score in sublist]
    average = sum(all_scores) / len(all_scores) if all_scores else 0  # Avoid division by zero
    print("Average score:", average)

file.close()
