
import string

# Define the function to calculate average
def calculate_average(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    scores = []  # This will hold all the scores

    for line in lines:
        # Clean the line and split by commas
        tempArray = line.strip().split(',')
        # Extract the scores (ignoring the name)
        score_list = list(map(int, tempArray[1:]))  # Convert score strings to integers
        scores.append(score_list)  # Add the list of scores to the scores list

    # Calculate the average for each class
    num_classes = len(scores[0])  # Assuming all classes have the same number of scores
    averages = []
    for i in range(num_classes):
        class_total = sum(score[i] for score in scores)
        class_average = class_total / len(scores)
        averages.append(class_average)

    return averages

# Use the function with your text file
averages = calculate_average("Class1.txt")
print("Average scores for each class:", averages)
