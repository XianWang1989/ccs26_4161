
import string

# Read the file
file = open("Class1.txt", "r")
lines = file.readlines()
file.close()

# Store the results
resultsArray = []

# Process each line
for line in lines:
    new_line = line.strip()  # Remove whitespace and newline
    tempArray = new_line.split(',')  # Split by comma
    name = tempArray[0]  # Store the name
    scores = list(map(int, tempArray[1:]))  # Convert scores to integers

    # Calculate the average
    average = sum(scores) / len(scores)  # Average calculation
    resultsArray.append((name, average))  # Append name and average to results

# Output the results
for name, avg in resultsArray:
    print(f"{name}'s average score is: {avg:.2f}")
