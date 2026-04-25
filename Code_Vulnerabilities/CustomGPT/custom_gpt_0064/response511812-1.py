
import string

# Function to calculate averages
def calculate_average(data):
    totals = []
    for entry in data:
        scores = list(map(int, entry[1:]))  # Convert score strings to integers
        totals.append(sum(scores) / len(scores))  # Calculate average for each entry
    return totals

# Read data from file
with open("Class1.txt", "r") as file:
    lines = file.readlines()

# Process data
resultsArray = []
for line in lines:
    stripped_line = line.strip()
    tempArray = stripped_line.split(',')
    resultsArray.append(tempArray)  # Store entries

# Ask user for output option
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")

if Option == "average score":
    averages = calculate_average(resultsArray)
    for name, avg in zip(resultsArray, averages):
        print(f"{name[0]}: Average Score = {avg:.2f}")
