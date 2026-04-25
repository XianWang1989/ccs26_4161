
import string

# Options for sorting or calculating
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options) + ": ")
file = open("Class1.txt", "r")

# Read and process the data
lines = file.readlines()
results_array = []

for line in lines:
    # Clean the line and split into components
    new_line = line.strip()
    temp_array = new_line.split(',')

    # Extract name and scores
    name = temp_array.pop(0)
    scores = [int(score) for score in temp_array]  # Convert scores to integers

    # Append to results array
    results_array.append((name, scores))

# Calculate average scores if selected
if option == "average score":
    for name, scores in results_array:
        average = sum(scores) / len(scores)  # Calculate average score
        print(f"{name}: Average score = {average:.2f}")

file.close()
