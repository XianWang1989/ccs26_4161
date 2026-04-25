
# Import necessary module
import string

# Define the options
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")

# Open the text file
file = open("Class1.txt", "r")
lines = file.readlines()

# Initialize variables for averaging
total_scores = []
num_classes = 0

# Process the lines in the file
for line in lines:
    new_line = line.strip()
    tempArray = new_line.split(',')
    scores = list(map(int, tempArray[1:]))  # Convert scores to integers
    total_scores.append(scores)  # Append scores to the total scores
    num_classes += 1  # Count the number of classes

# Calculate the average if the option is selected
if Option == "average score":
    all_scores = [score for sublist in total_scores for score in sublist]
    average = sum(all_scores) / len(all_scores) if all_scores else 0  # Average calculation
    print("Average score:", average)

# Close the file
file.close()
