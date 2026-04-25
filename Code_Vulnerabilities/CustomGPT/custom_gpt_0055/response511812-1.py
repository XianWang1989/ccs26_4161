
# Corrected code to calculate averages from the text file

import string

# Get user input for the output option
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options) + ": ")

# Read data from the file
file = open("Class1.txt", "r")
lines = file.readlines()
file.close()

# Initialize total score and count of scores for average calculation
total_scores = []
names = []

# Process each line in the file
for line in lines:
    # Strip newline and split by commas
    parts = line.strip().split(',')
    name = parts[0]

    # Convert scores to integers and calculate total
    scores = list(map(int, parts[1:]))
    total_scores.append(sum(scores))
    names.append(name)

# Calculate averages if the selected option is "average score"
if option == "average score":
    averages = [total / len(parts[1:]) for total in total_scores]

    # Print the names with their corresponding averages
    for name, avg in zip(names, averages):
        print(f"{name}: Average Score = {avg:.2f}")

# Additional output options (alphabetical order and highest to lowest)
elif option == "alphabetical order":
    for name in sorted(names):
        print(name)

elif option == "highest to lowest":
    sorted_scores = sorted(zip(names, total_scores), key=lambda x: x[1], reverse=True)
    for name, total in sorted_scores:
        print(f"{name}: Total Score = {total}")
