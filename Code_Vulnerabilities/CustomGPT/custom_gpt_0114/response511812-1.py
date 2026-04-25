
import string

# Function to calculate the average of scores
def calculate_average(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    total_scores = []
    # Loop through each line in the file
    for line in lines:
        # Strip newlines and split by commas
        tempArray = line.strip().split(',')
        # The name is the first element, scores are the rest
        scores = list(map(int, tempArray[1:]))  # Convert scores to integers
        total_scores.append(scores)

    return total_scores

# Function to compute averages
def compute_averages(scores_list):
    averages = []
    for scores in scores_list:
        avg = sum(scores) / len(scores)
        averages.append(avg)
    return averages

# Main function
file_path = "Class1.txt"
scores_list = calculate_average(file_path)
averages = compute_averages(scores_list)

print("Average scores:", averages)
