
import string

# Options to output
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? (Options: {}) ".format(options))

# Read the data from the text file
file = open("Class1.txt", "r")
lines = file.readlines()
results_array = []

# Process each line in the file
for line in lines:
    line = line.strip()  # Remove any leading/trailing whitespace
    temp_array = line.split(',')  # Split by comma
    name = temp_array.pop(0)  # Remove the name
    scores = list(map(int, temp_array))  # Convert scores to integers
    results_array.append(scores)  # Add scores to the results array

# Calculate average if the option is selected
if option == "average score":
    averages = []
    for scores in results_array:
        avg = sum(scores) / len(scores)
        averages.append(avg)
    print("Averages:", averages)

# Close the file
file.close()
