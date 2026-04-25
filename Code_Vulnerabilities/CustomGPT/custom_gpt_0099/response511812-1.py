
import string

# Function to calculate averages
def calculate_average(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    averages = []

    for line in lines:
        # Strip newline and split the line
        data = line.strip().split(',')
        # Convert the scores to integers and calculate the average
        scores = list(map(int, data[1:]))  # Skip the name and convert to int
        average = sum(scores) / len(scores)
        averages.append((data[0], average))  # Store name and average

    return averages

# Example usage
averages = calculate_average("Class1.txt")
for name, avg in averages:
    print(f"{name}: Average Score = {avg:.2f}")
