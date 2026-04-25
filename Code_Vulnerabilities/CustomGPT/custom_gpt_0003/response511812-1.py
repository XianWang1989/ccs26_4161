
import string

# Function to read data from file and calculate averages
def calculate_averages(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    results = []

    for line in lines:
        # Strip newline characters and split by comma
        tempArray = line.strip().split(',')

        # Extract scores and convert them to integers
        scores = list(map(int, tempArray[1:]))  # Convert scores to integers

        # Calculate the average if there are scores
        if scores:
            average_score = sum(scores) / len(scores)
            results.append((tempArray[0], average_score))  # Store name and average

    return results

# Example of how to use the function
averages = calculate_averages("Class1.txt")

# Print the results
for name, avg in averages:
    print(f"Average score for {name}: {avg:.2f}")
