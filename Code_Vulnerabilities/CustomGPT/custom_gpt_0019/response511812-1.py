
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options))
file = open("Class1.txt", "r")

# Initialize lists to store scores
scores = []

# Read lines and process them
lines = file.readlines()
for line in lines:
    new_line = line.strip()
    tempArray = new_line.split(',')
    name = tempArray.pop(0)  # Get name, we won't store it
    scores_list = [int(score) for score in tempArray]  # Convert scores to integers
    scores.append(scores_list)

# Calculate the average if the option is selected
if Option == "average score":
    average_scores = [sum(score) / len(score) for score in scores]
    print("Average scores:", average_scores)

# Close the file
file.close()
