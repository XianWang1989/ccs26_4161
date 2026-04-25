
import string

# Options for output
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options))

file = open("Class1.txt", "r")
lines = file.readlines()

# Initialize a list for storing scores
scores = []

# Process each line in the file
for line in lines:
    # Strip newline and split by comma
    parts = line.strip().split(',')

    # Convert the scores to integers and append to scores list
    scores.append([int(part) for part in parts[1:]])  # Skip the name

# Calculate averages if selected
if option == "average score":
    class_averages = [sum(score_list) / len(score_list) for score_list in zip(*scores)]
    print("Average scores for each column:", class_averages)

file.close()
