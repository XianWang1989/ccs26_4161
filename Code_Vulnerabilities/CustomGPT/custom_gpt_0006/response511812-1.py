
import string

# Function to read data and calculate averages
def calculate_average(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    scores = []

    for line in lines:
        new_line = line.strip()  # Remove any trailing newline characters
        tempArray = new_line.split(',')

        # Extract scores and convert to integers
        scores_list = list(map(int, tempArray[1:]))  # Convert scores to integers
        scores.append(scores_list)

    # Calculate averages for each class
    averages = []
    for score_list in scores:
        if score_list:  # Check if the list is not empty
            average_score = sum(score_list) / len(score_list)
            averages.append(average_score)

    return averages

# Example usage
filename = "Class1.txt"
averages = calculate_average(filename)
print("Average scores for each class:", averages)
