
import string

# Define options and prompt for user choice
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options) + ": ")

# Read data from the file
file = open("Class1.txt", "r")
lines = file.readlines()
file.close()

# Initialize variables to store scores
all_scores = []

# Process each line in the file
for line in lines:
    line = line.strip()  # Remove any trailing newline
    temp_array = line.split(',')
    name = temp_array[0]  # Get the name
    scores = list(map(int, temp_array[1:]))  # Convert scores to integers
    all_scores.append(scores)  # Store scores for averaging later

# Calculate average scores if the user selected "average score"
if option == "average score":
    averages = []

    for scores in all_scores:
        avg = sum(scores) / len(scores)  # Compute average for each student
        averages.append(avg)

    # Print each average score
    for idx, avg in enumerate(averages, start=1):
        print(f"Average score for Class {idx}: {avg:.2f}")
