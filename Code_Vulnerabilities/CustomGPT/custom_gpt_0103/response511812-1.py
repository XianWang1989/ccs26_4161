
# Open the file and read lines
file = open("Class1.txt", "r")
lines = file.readlines()
file.close()

# Initialize variables
total_scores = []
num_scores = 0

# Process each line
for line in lines:
    # Strip whitespace and split the line
    parts = line.strip().split(',')
    # Convert scores to integers and collect them
    scores = list(map(int, parts[1:]))  # Convert scores to integers
    total_scores.append(scores)
    num_scores += len(scores)

# Compute average
if total_scores:
    # Flatten the list of scores
    all_scores = [score for sublist in total_scores for score in sublist]
    average = sum(all_scores) / len(all_scores) if all_scores else 0
    print("Average score:", average)
else:
    print("No scores available.")
