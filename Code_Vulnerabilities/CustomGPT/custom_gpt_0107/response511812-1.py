
import string

# Define the file name
filename = "Class1.txt"

# Function to calculate averages
def calculate_averages(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    averages = []
    for line in lines:
        # Clean the line and split into components
        components = line.strip().split(',')
        name = components[0]  # Get the name
        scores = list(map(int, components[1:]))  # Convert scores to integers

        # Calculate average
        average = sum(scores) / len(scores)
        averages.append((name, average))

    return averages

# Main execution
if __name__ == "__main__":
    averages = calculate_averages(filename)

    # Print the averages
    for name, avg in averages:
        print(f"{name}: Average Score = {avg:.2f}")
