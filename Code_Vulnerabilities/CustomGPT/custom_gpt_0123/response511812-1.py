
import string

# Define options
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options))

# Initialize lists to hold scores
scores = []

# Open file and read lines
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Process each line
for line in lines:
    line = line.strip()  # Remove trailing newline
    tempArray = line.split(',')

    # Extract scores (convert them to integers)
    scores.append(list(map(int, tempArray[1:])))  # Skip the name

# Calculate the average if the option is "average score"
if option == "average score":
    averages = []
    for score_list in scores:
        average = sum(score_list) / len(score_list)
        averages.append(average)

    print("Average Scores:", averages)
