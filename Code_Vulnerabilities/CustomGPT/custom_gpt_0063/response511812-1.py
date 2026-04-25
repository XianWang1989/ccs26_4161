
# Reading data from the text file and calculating averages
import string

# Change 'Class1.txt' to your actual file if needed
file = open("Class1.txt", "r")
lines = file.readlines()

# Initialize sum and count
total_sum = 0
count = 0

# Process each line
for line in lines:
    # Clean and split the line
    entry = line.strip()
    tempArray = entry.split(',')

    # Extract scores and convert them to integers
    scores = list(map(int, tempArray[1:]))  # Skip the name and convert scores to int
    total_sum += sum(scores)  # Add to total sum
    count += len(scores)  # Count the number of scores

# Calculate average
if count > 0:
    average = total_sum / count
else:
    average = 0

print("Average score:", average)

file.close()
