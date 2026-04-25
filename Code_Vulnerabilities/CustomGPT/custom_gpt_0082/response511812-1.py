
# Reading data from the file
filename = "Class1.txt"

# Initialize lists to store scores
scores = []

# Open the file and read lines
with open(filename, "r") as file:
    lines = file.readlines()

# Process each line
for line in lines:
    # Strip whitespace and split by comma
    tempArray = line.strip().split(',')
    # Extract the scores as integers
    student_scores = list(map(int, tempArray[1:]))  # Skip the name
    scores.append(student_scores)

# Calculate averages for each student
averages = [sum(student_scores) / len(student_scores) for student_scores in scores]

# Output the average scores
for i, avg in enumerate(averages):
    print(f"Average score for Student {i + 1}: {avg}")
