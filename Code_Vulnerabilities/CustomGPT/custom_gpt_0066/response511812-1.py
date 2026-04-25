
# Function to calculate averages
def calculate_averages(filename):
    averages = []

    with open(filename, 'r') as file:
        for line in file:
            # Remove any leading/trailing whitespace and newlines
            data = line.strip().split(',')
            scores = list(map(int, data[1:]))  # Convert the scores to integers
            average = sum(scores) / len(scores)  # Calculate the average
            averages.append((data[0], average))  # Store name and average

    return averages

# Main execution
filename = "Class1.txt"
averages = calculate_averages(filename)

for name, avg in averages:
    print(f"{name}: Average Score = {avg:.2f}")
