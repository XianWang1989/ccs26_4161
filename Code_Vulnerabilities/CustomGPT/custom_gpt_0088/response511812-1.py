
import string

# Define the options
options = ["alphabetical order", "highest to lowest", "average score"]
option = input("Which order do you want to output? " + str(options))
filename = "Class1.txt"

# Read and process the file
with open(filename, "r") as file:
    lines = file.readlines()

results_array = []

# Parse each line
for line in lines:
    line = line.strip()  # Remove whitespace and newline characters
    temp_array = line.split(',')
    name = temp_array[0]
    scores = list(map(int, temp_array[1:]))  # Convert scores to integers
    results_array.append((name, scores))

# Calculate average if selected
if option == "average score":
    for name, scores in results_array:
        average = sum(scores) / len(scores)  # Calculate average
        print(f"{name}: Average Score = {average:.2f}")
