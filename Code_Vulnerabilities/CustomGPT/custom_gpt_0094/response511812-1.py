
import string

def calculate_average(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    scores = []

    for line in lines:
        # Clean and split the line
        line = line.strip()
        tempArray = line.split(',')

        # Extract scores, convert to integers and add to scores list
        scores.append(list(map(int, tempArray[1:])))  # skip name and convert scores to integers

    # Calculate the average for each list of scores
    averages = [sum(score_list) / len(score_list) for score_list in scores]

    return averages

# Usage
filename = "Class1.txt"
averages = calculate_average(filename)
print("Average scores:", averages)
