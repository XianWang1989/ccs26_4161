
# Import necessary library
import string

# Function to calculate averages
def calculate_averages(filename):
    results = []

    # Open the file and read lines
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Process each line
    for line in lines:
        # Remove whitespace and split by commas
        tempArray = line.strip().split(',')

        # Extract scores and convert to integers
        scores = list(map(int, tempArray[1:]))  # Convert the scores to integers
        results.append(scores)

    # Calculate the average scores for each class
    averages = [sum(scores) / len(scores) for scores in zip(*results)]  # Transpose and calculate average

    return averages

# Example usage
averages = calculate_averages("Class1.txt")
print("Average scores for each subject:", averages)
