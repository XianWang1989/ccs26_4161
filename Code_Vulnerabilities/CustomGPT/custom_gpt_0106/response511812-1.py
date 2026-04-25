
import string

# Options for sorting output
Options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(Options) + ": ")
filename = "Class1.txt"

# Read the data from the file
with open(filename, "r") as file:
    lines = file.readlines()

# Store the results in a list
results = []

# Process each line in the file
for line in lines:
    new_line = line.strip()  # Remove newline characters
    temp_array = new_line.split(',')  # Split by commas
    name = temp_array[0]  # Get the name
    scores = list(map(int, temp_array[1:]))  # Convert remaining to integers
    results.append((name, scores))  # Append name and scores as a tuple

# Calculate average scores if requested
if option == "average score":
    for name, scores in results:
        average = sum(scores) / len(scores)  # Calculate average
        print(f"{name}: Average score = {average}")

