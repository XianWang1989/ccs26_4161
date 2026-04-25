
import string

# Options for output order
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options) + ": ")
file = open("Class1.txt", "r")

# Initialize a list to store results
results = []

# Read lines from the file
lines = file.readlines()
for line in lines:
    # Strip newline and split
    tempArray = line.strip().split(',')
    name = tempArray.pop(0)  # Remove the name
    scores = list(map(int, tempArray))  # Convert scores to integers
    results.append(scores)

# Function to calculate average
def calculate_average(scores_list):
    all_scores = [score for scores in scores_list for score in scores]
    return sum(all_scores) / len(all_scores) if all_scores else 0

if option == "average score":
    average = calculate_average(results)
    print(f"Average score: {average}")

file.close()
