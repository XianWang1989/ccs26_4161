
import string

def calculate_average(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    total_scores = []  # List to store total scores for averaging
    total_count = 0    # Count of scores added

    for line in lines:
        # Process each line to extract scores
        new_line = line.strip()  # Remove newline characters
        temp_array = new_line.split(',')  # Split at commas
        scores = [int(score) for score in temp_array[1:]]  # Convert scores to integers

        # Add scores to the total list
        total_scores.extend(scores)
        total_count += len(scores)

    # Calculate the average if there are scores
    if total_count > 0:
        average = sum(total_scores) / total_count
        print(f"The average score is: {average:.2f}")
    else:
        print("No scores to average.")

# Call the function with the filename
calculate_average("Class1.txt")
