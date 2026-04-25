
def calculate_average(file_path):
    options = ("alphabetical order", "highest to lowest", "average score")
    option = input("Which order do you want to output? " + str(options) + ": ")

    with open(file_path, "r") as file:
        lines = file.readlines()

    results = []

    for line in lines:
        data = line.strip().split(',')
        name = data[0]
        scores = list(map(int, data[1:]))  # Convert scores to integers
        average_score = sum(scores) / len(scores)
        results.append((name, average_score))

    if option == "average score":
        for name, avg in results:
            print(f"{name}: {avg:.2f}")  # Formatting to 2 decimal places

# Call the function with the desired file
calculate_average("Class1.txt")
