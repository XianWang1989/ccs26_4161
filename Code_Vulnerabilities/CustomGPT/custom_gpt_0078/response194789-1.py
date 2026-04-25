
def foo(numbers):
    # Helper function to generate combinations
    def generate_combinations(index):
        if index == len(numbers):
            return [[]]  # Base case: return a list containing an empty list

        current_number = abs(numbers[index])  # Get the absolute value
        combinations = []

        # Recursively generate combinations for the next index
        for combination in generate_combinations(index + 1):
            combinations.append([current_number] + combination)   # Positive
            combinations.append([-current_number] + combination)  # Negative

        return combinations

    return generate_combinations(0)

# Examples
print(foo([-4]))          # [[4], [-4]]
print(foo([1, 1]))       # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))      # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))   # [[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1], [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]]
