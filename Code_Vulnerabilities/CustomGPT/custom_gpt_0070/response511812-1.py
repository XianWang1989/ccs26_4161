
import string

# Get user input for output options
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")

# Initialize variables
scores = []
file = open("Class1.txt", "r")

# Read lines from the file
lines = file.readlines()

# Process each line
for line in lines:
    clean_line = line.strip()  # Remove newline and extra spaces
    tempArray = clean_line.split(',')  # Split by comma
    # Convert scores to integers and append to scores list
    scores.append([int(score) for score in tempArray[1:]])

# Close the file
file.close()

# Calculate average if the selected option is "average score"
if Option == "average score":
    total_scores = [sum(score) for score in scores]
    average = sum(total_scores) / len(total_scores) if total_scores else 0
    print(f"Average score: {average}")
