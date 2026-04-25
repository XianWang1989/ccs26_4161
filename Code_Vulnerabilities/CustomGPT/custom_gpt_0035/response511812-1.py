
import string

def calculate_averages(filename):
    with open(filename, 'r') as file:
        total_scores = []
        for line in file:
            # Remove newline and split the line into parts
            parts = line.strip().split(',')
            scores = list(map(int, parts[1:]))  # Convert scores to integers
            total_scores.append(scores)  # Store the scores

        # Calculate averages
        averages = [sum(scores) / len(scores) for scores in total_scores]
        return averages

# File containing scores
filename = "Class1.txt"
averages = calculate_averages(filename)
print("Averages for each class:", averages)
