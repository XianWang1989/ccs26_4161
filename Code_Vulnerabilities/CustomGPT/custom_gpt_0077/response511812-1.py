
import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = input("Which order do you want to output? " + str(Options) + ": ")
file = open("Class1.txt", "r")

# Lists to hold scores
score_sums = []
score_counts = []

# Reading lines from the file
lines = file.readlines()
for line in lines:
    new_line = line.strip()
    tempArray = new_line.split(',')

    # Get the scores and convert to integers
    scores = list(map(int, tempArray[1:]))  # Convert score strings to integers
    score_sums.append(sum(scores))            # Total score for this line
    score_counts.append(len(scores))          # Count of scores

# Calculate the average score if selected
if Option == "average score":
    total_sum = sum(score_sums)
    total_count = sum(score_counts)
    average = total_sum / total_count if total_count > 0 else 0
    print(f"Average score: {average}")

file.close()
