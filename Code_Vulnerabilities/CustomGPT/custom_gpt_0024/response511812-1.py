
import string

def calculate_average(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    all_scores = []

    for line in lines:
        # Strip the line and split by commas
        stripped_line = line.strip()
        temp_array = stripped_line.split(',')

        # Collect scores from the line (ignoring the name)
        scores = list(map(int, temp_array[1:]))  # Convert scores to integers
        all_scores.append(scores)

    # Calculate the averages for each set of scores
    averages = []
    for scores in all_scores:
        avg = sum(scores) / len(scores)  # Calculate average
        averages.append(avg)

    return averages

# Example usage
averages = calculate_average("Class1.txt")
print("Averages:", averages)
