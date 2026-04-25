
import string

# Options for output
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options) + ": ")
file = open("Class1.txt", "r")

# Prepare to collect scores
scores = []

# Read the lines from the file
lines = file.readlines()

for line in lines:
    line = line.strip()  # Remove whitespace and newline
    tempArray = line.split(',')  # Split by comma
    name = tempArray[0]  # First element is the name
    scores_list = [int(score) for score in tempArray[1:]]  # Convert scores to integers
    scores.append(scores_list)  # Collect scores

# Calculate averages if selected
if option == "average score":
    averages = [sum(score) / len(score) for score in scores]  # Average for each list of scores
    print("Average scores:", averages)

# Optional: Print the results in a specific order
if option == "alphabetical order":
    print(sorted([line.strip() for line in lines], key=lambda x: x.split(',')[0]))
elif option == "highest to lowest":
    print(sorted(scores, key=lambda x: sum(x), reverse=True))

file.close()
