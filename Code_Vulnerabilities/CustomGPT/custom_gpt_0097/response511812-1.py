
import string

# Define options for output
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options))

# Read data from the file
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Initialize a list to store scores
all_scores = []

for line in lines:
    # Strip whitespace and split the line into components
    new_line = line.strip()
    temp_array = new_line.split(',')

    # Extract scores and convert to integers
    scores = list(map(int, temp_array[1:]))  # Skip the name
    all_scores.append(scores)

# Calculate the average score if the user selected "average score"
if option == "average score":
    averages = [sum(scores) / len(scores) for scores in all_scores]
    print("Average scores:", averages)
