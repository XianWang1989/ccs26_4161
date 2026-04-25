import string

Options = ("alphabetical order", "highest to lowest", "average score")
Option = raw_input("Which order do you want to output?" + str(Options))
choices = ("Class 1", "Class 2", "Class 3")

# Open the file
file = open("Class1.txt", "r")

lines = file.readlines()
file.close()  # Don't forget to close the file

# Initialize a list to store the results
resultsArray = []

# Process each line in the file
for line in lines:
    # Clean up the line and split it into values
    new_line = line.strip()  # Remove trailing newlines
    tempArray = new_line.split(',')  # Split by comma
    name = tempArray[0]  # First item is the name
    scores = list(map(int, tempArray[1:]))  # Convert the remaining items to integers (scores)
    
    # Calculate the average score
    average_score = sum(scores) / len(scores)  # Sum of scores divided by the number of scores
    
    # Append the name and the average score to the results
    resultsArray.append((name, average_score))

# If the option chosen is "average score", print the averages
if Option == "average score":
    for name, avg in resultsArray:
        print(f"{name}: {avg:.2f}")  # Print each student's average score rounded to 2 decimal places
