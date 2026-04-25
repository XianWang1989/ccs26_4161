
import string

# Options for output
Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")

# Initialize an array to store scores
scores = []

# Open the file and read lines
with open("Class1.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        # Clean the line and split into parts
        new = line.strip()  # Remove whitespace and newline characters
        tempArray = new.split(',')  # Split by commas

        # Extract the name and scores
        name = tempArray.pop(0)  # Remove the name from the list
        score_list = [int(score) for score in tempArray]  # Convert scores to integers

        # Add the scores to the main list
        scores.append(score_list)

# Calculate average if chosen option is 'average score'
if Option == "average score":
    if scores:  # Check if the scores list is not empty
        sum_scores = [0] * len(scores[0])  # Initialize sum for each score
        for score_set in scores:
            for index in range(len(score_set)):
                sum_scores[index] += score_set[index]

        average_scores = [total / len(scores) for total in sum_scores]  # Calculate average

        print("Average scores:", average_scores)  # Output the average scores
