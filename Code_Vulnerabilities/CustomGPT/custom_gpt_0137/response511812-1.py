
def calculate_averages(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Initialize an array to hold the scores
    all_scores = []

    for line in lines:
        # Strip the newline character and split the line into components
        parts = line.strip().split(',')
        # Extract only the scores (the last three parts)
        scores = list(map(int, parts[1:]))  # Convert scores to integers
        all_scores.append(scores)  # Append to the list of scores

    return all_scores

def calculate_average(scores):
    # Calculate the average of scores
    total = sum(scores)
    average = total / len(scores) if scores else 0
    return average

# Main execution
file_name = "Class1.txt"
all_scores = calculate_averages(file_name)

# Now, calculate averages for each student
for index, scores in enumerate(all_scores):
    avg_score = calculate_average(scores)
    print(f"Average score for Class {index + 1}: {avg_score:.2f}")

# Additional average for the entire class
# Flatten the list of all scores for everyone and calculate the overall average
flat_scores = [score for sublist in all_scores for score in sublist]
overall_average = calculate_average(flat_scores)
print(f"Overall average score: {overall_average:.2f}")
