
import string

# Options for output
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options) + ": ")

# Open the file
file = open("Class1.txt", "r")
lines = file.readlines()

# Initialize variables for average computation
total = 0
count = 0

# Process each line in the file
for line in lines:
    line = line.strip()  # Remove any leading/trailing whitespace
    temp_array = line.split(',')  # Split the line into components
    scores = list(map(int, temp_array[1:]))  # Convert scores to integers

    # Calculate total and count for average
    total += sum(scores)
    count += len(scores)

    # Print the printed array (if needed)
    print(temp_array)  # You can modify it to print scores if required

# Calculate the average
if option == "average score":
    average = total / count  # Total scores divided by number of scores
    print("Average score:", average)

file.close()
