
import string

# Initialize options
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options))
file = open("Class1.txt", "r")

# Initialize variables for average calculation
total_sum = 0
count = 0

# Read each line in the file
for line in file:
    # Clean up the line and split into components
    line = line.strip()
    tempArray = line.split(',')

    # Extract scores and convert to integers
    scores = list(map(int, tempArray[1:]))  # Convert string scores to integers

    # Calculate the sum and increment count
    total_sum += sum(scores)
    count += len(scores)

    # If you want to print the individual scores
    print(f"Scores for {tempArray[0]}: {scores}")

# Calculate the average if the option chosen is "average score"
if Option == "average score":
    average = total_sum / count if count > 0 else 0  # Avoid division by zero
    print("Average score:", average)

file.close()
