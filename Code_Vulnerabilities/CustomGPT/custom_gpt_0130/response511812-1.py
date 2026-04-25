
# Import necessary modules
import string

# Options for output
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options))

# Open the data file
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Prepare to store scores
scores = []

# Process each line in the file
for line in lines:
    # Clean and split the line into components
    line = line.strip()  # Remove newline characters
    tempArray = line.split(',')

    # Get scores as integers
    int_scores = list(map(int, tempArray[1:]))  # Convert scores to integers
    scores.append(int_scores)

# Calculate average if the chosen option is "average score"
if option == "average score":
    total_scores = [sum(score) for score in scores]  # Sum of each student's scores
    average = sum(total_scores) / len(total_scores)  # Calculate average score
    print(f"Average score: {average:.2f}")

# Optional: Handle other options here (alphabetical, highest to lowest)
