
import string

# Options for output
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options))

# Initialize variables
scores = []

# Read data from file
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Process each line
for line in lines:
    cleaned_line = line.strip()
    tempArray = cleaned_line.split(',')

    # Convert scores from strings to integers
    scores_list = [int(score) for score in tempArray[1:]]  # Skip the name
    scores.append(scores_list)

# Calculate average if the option is selected
if option == "average score":
    total_scores = [sum(student_scores) for student_scores in scores]
    average = sum(total_scores) / len(total_scores)
    print("Average score:", average)
