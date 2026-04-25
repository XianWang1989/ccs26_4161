
import string

# Define options for output
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options))

# Read data from the file
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Initialize a list to store averages
averages = []

# Process each line in the file
for line in lines:
    # Clean and split the line
    line = line.strip()
    temp_array = line.split(',')

    # Extract name and scores
    name = temp_array[0]
    scores = list(map(int, temp_array[1:]))  # Convert scores to integers

    # Calculate average
    average_score = sum(scores) / len(scores)
    averages.append((name, average_score))

# Output averages based on the selected option
if option == "average score":
    for name, avg in averages:
        print(f"{name}: {avg:.2f}")
