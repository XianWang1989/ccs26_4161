
import string

# Options for output
options = ("alphabetical order", "highest to lowest", "average score")
option = input("Which order do you want to output? " + str(options) + ": ")
choices = ("Class 1", "Class 2", "Class 3")

# Open the file containing scores
with open("Class1.txt", "r") as file:
    lines = file.readlines()

    # Prepare to store results
    results_array = []

    # Process each line in the file
    for line in lines:
        # Clean and split the line into components
        cleaned_line = line.strip()
        temp_array = cleaned_line.split(',')

        # Extract name and scores
        name = temp_array[0]  # First element is the name
        scores = list(map(int, temp_array[1:]))  # Convert the rest to integers

        # Append to results
        results_array.append((name, scores))

    # Calculate averages if the selected option is "average score"
    if option == "average score":
        averages = []

        for name, scores in results_array:
            avg = sum(scores) / len(scores)  # Calculate the average
            averages.append((name, avg))  # Store name and average score

        # Print the averages
        for name, avg in averages:
            print(f"{name}: Average Score = {avg:.2f}")
