
import string

# Function to calculate the average
def calculate_average(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    results = []

    # Process each line in the text file
    for line in lines:
        # Strip whitespace and split the line by commas
        data = line.strip().split(',')

        # Get the scores by converting to integers
        scores = list(map(int, data[1:]))  # Ignore the name and convert the scores to integers

        # Append the scores to results
        results.append(scores)

    # Calculate the average for each list of scores
    averages = []
    for score_list in results:
        average = sum(score_list) / len(score_list)
        averages.append(average)

    return averages

# Example usage
filename = "Class1.txt"
averages = calculate_average(filename)
print("Averages:", averages)
