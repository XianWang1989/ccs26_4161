
import string

# Function to calculate averages
def calculate_averages(filename):
    averages = []

    with open(filename, "r") as file:
        lines = file.readlines()

        for line in lines:
            # Strip newline characters and split by commas
            tempArray = line.strip().split(',')
            name = tempArray[0]  # Get the student's name
            scores = list(map(int, tempArray[1:]))  # Convert scores to integers

            # Calculate the average
            avg_score = sum(scores) / len(scores)
            averages.append((name, avg_score))

    return averages

# Example usage
averages = calculate_averages("Class1.txt")

# Print the results
for name, avg in averages:
    print(f"{name}'s average score: {avg:.2f}")
