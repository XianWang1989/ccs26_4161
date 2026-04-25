
# Import necessary modules
import string

# Define options for output
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options))

# Open the file containing class data
file = open("Class1.txt", "r")

# Initialize an array to hold the scores
scores = []

# Read lines from the file
lines = file.readlines()

# Process each line in the file
for line in lines:
    # Strip newline characters and split the line into components
    parts = line.strip().split(',')
    # Convert the scores (excluding the name) to integers and add to scores list
    scores.append([int(x) for x in parts[1:]])

# Close the file
file.close()

# Check what option was chosen
if option == "average score":
    # Calculate average scores for each student
    averages = [sum(score_list) / len(score_list) for score_list in scores]
    print("Average scores:", averages)
