
import string

# Getting the user's choice for output order
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options) + ": ")

# Initialize variables
scores = []

# Open the file and read lines
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Process each line
for line in lines:
    new_line = line.strip()  # Remove newline characters
    temp_array = new_line.split(',')  # Split by comma
    name = temp_array.pop(0)  # Get the name
    scores_list = list(map(int, temp_array))  # Convert scores to integers
    scores.append(scores_list)  # Add the scores to the main list

# Calculate averages if the user chose "average score"
if option == "average score":
    # Calculate the average for each list of scores
    averages = [sum(score) / len(score) for score in scores]
    print("Average scores:", averages)
