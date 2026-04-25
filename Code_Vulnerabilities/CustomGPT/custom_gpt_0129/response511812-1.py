
import string

# Function to calculate average scores from the provided data
def calculate_average(file_name):
    results = []

    with open(file_name, "r") as file:
        lines = file.readlines()

        for line in lines:
            # Clean the line and split by comma
            new_line = line.strip()
            tempArray = new_line.split(',')

            # Extract name and scores
            name = tempArray.pop(0)  # Remove the name from the list
            scores = list(map(int, tempArray))  # Convert the remaining items to integers

            # Calculate average
            if scores:  # Check if there's anything to average
                average = sum(scores) / len(scores)
                results.append((name, average))

    return results

# Use the function to get averages
averages = calculate_average("Class1.txt")

# Print the results
for name, avg in averages:
    print(f"{name}'s average score is {avg:.2f}")
