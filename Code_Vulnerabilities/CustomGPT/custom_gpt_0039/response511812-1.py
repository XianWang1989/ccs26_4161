
import string

# Options for output format
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options) + ": ")

# Open the file containing class scores
file = open("Class1.txt", "r")
lines = file.readlines()
file.close()

# Initialize a list to hold scores
scores = []

# Process each line in the file
for line in lines:
    # Strip newline characters and split the line into components
    elements = string.strip(line, '\n').split(',')
    name = elements[0]  # Get the name
    # Convert scores to integers and add to the scores list
    score_list = [int(score) for score in elements[1:]]
    scores.append(score_list)

# Calculate the average if needed
if option == "average score":
    total_sum = 0
    count = 0

    # Iterate through each list of scores
    for score_list in scores:
        total_sum += sum(score_list)  # Sum all scores
        count += len(score_list)  # Count total number of scores

    # Calculate average
    average = total_sum / count if count > 0 else 0
    print("Average score:", average)
