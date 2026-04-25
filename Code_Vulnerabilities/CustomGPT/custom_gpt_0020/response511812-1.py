
import string

def calculate_average(scores):
    """Calculate the average of a list of scores."""
    return sum(scores) / len(scores) if scores else 0

def main():
    # Options for output
    options = ("alphabetical order", "highest to lowest", "average score")
    option = input("Which order do you want to output? " + str(options))

    # Read data from file
    with open("Class1.txt", "r") as file:
        lines = file.readlines()

    # Store results
    scores_dict = {}

    for line in lines:
        cleaned_line = line.strip()  # Remove newline and extra spaces
        temp_array = cleaned_line.split(',')

        # Extract name and scores
        name = temp_array[0]
        scores = [int(n) for n in temp_array[1:] if n.isdigit()]  # Convert scores to integers

        # Store scores in dictionary
        scores_dict[name] = scores

        # Printing for debugging (you can remove it later)
        print(f"{name}: {scores}")

    # Calculate and show averages if the selected option is 'average score'
    if option == "average score":
        for name, scores in scores_dict.items():
            average = calculate_average(scores)
            print(f"{name}'s average score: {average}")

if __name__ == "__main__":
    main()
