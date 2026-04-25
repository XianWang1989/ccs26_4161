
import string

# Function to calculate the average score
def calculate_average(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    total_sum = 0
    count = 0

    for line in lines:
        # Strip the newline and split the line into components
        parts = line.strip().split(',')

        # Extract scores, converting them to integers and calculate the sum and count
        scores = list(map(int, parts[1:]))  # Convert score strings to integers
        total_sum += sum(scores)
        count += len(scores)

    # Calculate and return the average
    average = total_sum / count if count > 0 else 0
    return average

# Main execution
file_path = "Class1.txt"  # Specify the path to your text file here
average_score = calculate_average(file_path)
print("The average score is:", average_score)
