
import string

# Define options
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")
choices = ("Class 1", "Class 2", "Class 3")

# Read the file
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Initialize a list for storing results
results = []

# Process each line in the file
for line in lines:
    new_line = line.strip()  # Remove newline characters
    tempArray = new_line.split(',')  # Split to get name and scores
    name = tempArray.pop(0)  # Get the name
    scores = [int(score) for score in tempArray]  # Convert scores to integers
    results.append((name, scores))  # Append name and scores as a tuple

# Calculate and print averages if the option is selected
if Option == "average score":
    for name, scores in results:
        average = sum(scores) / len(scores)  # Calculate the average
        print(f"{name}: Average Score = {average:.2f}")

