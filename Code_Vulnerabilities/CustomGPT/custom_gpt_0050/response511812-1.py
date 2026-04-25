
import string

# Function to calculate average
def calculate_average(scores):
    return sum(scores) / len(scores)

# Read data from the file
file = open("Class1.txt", "r")
lines = file.readlines()
file.close()

# Lists to store names and their scores
names = []
scores_list = []

for line in lines:
    # Process each line
    line = line.strip()  # Remove any trailing whitespace
    tempArray = line.split(',')
    names.append(tempArray[0])  # Store the name
    scores = list(map(int, tempArray[1:]))  # Convert scores to integers
    scores_list.append(scores)

# Calculate the average score for each student
averages = [calculate_average(scores) for scores in scores_list]

# Print results
for name, average in zip(names, averages):
    print(f"{name}'s average score: {average:.2f}")

# Example of handling a specific option (average score)
option = input("Which order do you want to output? (average score): ")
if option == "average score":
    print("Average scores:")
    for name, average in zip(names, averages):
        print(f"{name}: {average:.2f}")
