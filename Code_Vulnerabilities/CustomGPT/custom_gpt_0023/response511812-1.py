
import string

# Get user input for ordering
options = ["alphabetical order", "highest to lowest", "average score"]
option = input("Which order do you want to output? " + str(options) + ": ")

# Read data from the text file
with open("Class1.txt", "r") as file:
    lines = file.readlines()

results = []

# Process each line in the text file
for line in lines:
    # Strip newline and whitespace, then split by commas
    stripped_line = line.strip()
    temp_array = stripped_line.split(',')

    # Extract the name and scores
    name = temp_array[0]
    scores = list(map(int, temp_array[1:]))  # Convert score strings to integers

    # Append name and scores to results
    results.append((name, scores))

# Calculate averages
if option == "average score":
    averages = []
    for name, scores in results:
        avg_score = sum(scores) / len(scores)  # Calculate average for each student
        averages.append((name, avg_score))

    # Print the averages
    for name, avg in averages:
        print(f"{name}: Average score = {avg:.2f}")
