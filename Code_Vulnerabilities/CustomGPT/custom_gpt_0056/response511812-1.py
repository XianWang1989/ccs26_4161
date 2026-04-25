
import string

# Function to calculate average scores from file
def calculate_averages(filename):
    averages = []

    with open(filename, "r") as file:
        lines = file.readlines()

        for line in lines:
            # Clean and split the line
            data = string.strip(line, '\n').split(',')
            name = data[0]  # Extract name
            scores = list(map(int, data[1:]))  # Convert scores to integers

            # Calculate average
            average_score = sum(scores) / len(scores)
            averages.append((name, average_score))

    return averages

# Main execution
def main():
    filename = "Class1.txt"
    averages = calculate_averages(filename)

    for name, avg in averages:
        print(f"{name}: Average Score = {avg:.2f}")

# Run the program
if __name__ == "__main__":
    main()
