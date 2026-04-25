
import string

def calculate_average(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    total_scores = []
    for line in lines:
        line = line.strip()
        if line:  # ensure line is not empty
            parts = line.split(',')
            scores = [int(score) for score in parts[1:]]
            total_scores.append(sum(scores))

    # Calculate the average
    if total_scores:
        average = sum(total_scores) / len(total_scores)
        print("Average score:", average)
    else:
        print("No scores found.")

# Calling the function with your text file
calculate_average("Class1.txt")
