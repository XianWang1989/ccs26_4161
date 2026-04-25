
import string

def calculate_average(filename):
    # Open the file
    with open(filename, "r") as file:
        lines = file.readlines()

    total_score = 0
    count = 0

    for line in lines:
        # Clean and parse the line
        line = line.strip()
        tempArray = line.split(',')

        # Get the scores and convert them to integers
        scores = list(map(int, tempArray[1:]))  # Ignore the name
        total_score += sum(scores)
        count += len(scores)

    # Calculate the average
    average = total_score / count if count else 0
    return average

# Specify the filename
filename = "Class1.txt"
average_score = calculate_average(filename)
print("The average score is:", average_score)
