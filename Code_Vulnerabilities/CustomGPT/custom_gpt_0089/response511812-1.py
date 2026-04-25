
import string

# Options
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options))

# Open the file
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Initialize lists to track sums and counts for averages
scores_list = []

# Process each line in the file
for line in lines:
    # Clean up the string
    clean_line = line.strip()
    # Split into name and scores
    parts = clean_line.split(',')
    name = parts[0]
    # Convert scores to integers and store
    scores = list(map(int, parts[1:]))
    scores_list.append(scores)

# Calculate average if the option is selected
if option == "average score":
    for i, scores in enumerate(scores_list):
        average = sum(scores) / len(scores)
        print(f"Average score for student {i + 1}: {average:.2f}")

# Add other options as needed
