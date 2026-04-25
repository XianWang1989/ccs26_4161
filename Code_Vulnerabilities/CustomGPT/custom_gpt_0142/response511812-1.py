
# Improved code to calculate averages from a text file of scores

def calculate_averages(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        # Initialize a list to hold the averages
        averages = []

        for line in lines:
            # Split the line into a list and remove any whitespace
            parts = line.strip().split(',')
            # Extract the scores as integers
            scores = list(map(int, parts[1:]))  # Convert strings to integers (skip the name)
            # Calculate the average
            average = sum(scores) / len(scores) if scores else 0
            # Append the average to the averages list
            averages.append((parts[0], average))  # Store name and average

        return averages

# File containing the data
filename = "Class1.txt"
averages = calculate_averages(filename)

# Optionally print the averages
for name, avg in averages:
    print(f"{name}: Average Score = {avg:.2f}")
