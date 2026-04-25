
import string

def read_scores(filename):
    results = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            # Strip newlines and split by commas
            data = line.strip().split(',')
            # Convert scores to integers
            scores = [int(x) for x in data[1:]]
            results.append(scores)
    return results

def calculate_average(scores):
    averages = []
    for score_list in scores:
        if score_list:  # Ensure the list is not empty
            average = sum(score_list) / len(score_list)
            averages.append(average)
    return averages

# Main program flow
scores = read_scores("Class1.txt")
average_scores = calculate_average(scores)

print("Average scores:", average_scores)
