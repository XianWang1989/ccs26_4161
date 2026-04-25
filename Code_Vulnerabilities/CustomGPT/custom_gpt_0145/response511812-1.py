
import string

# Define the function to calculate average
def calculate_average(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    total_scores = []
    for line in lines:
        # Strip newline characters and split by comma
        tempArray = line.strip().split(',')
        # Extract scores and convert them to integers
        scores = [int(score) for score in tempArray[1:]]  # Get scores ignoring the name
        total_scores.append(scores)

    # Calculate average for each class
    averages = []
    for scores in total_scores:
        average = sum(scores) / len(scores)  # Calculate average
        averages.append(average)

    return averages

# Call the function and print the results
averages = calculate_average("Class1.txt")
print("Average scores for each class:", averages)

# Optionally, if you want to output differently based on user choice
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options))

if Option == "average score":
    print("Class averages:", averages)
