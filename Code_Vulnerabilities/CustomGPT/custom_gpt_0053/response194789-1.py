
def foo(numbers):
    # Helper function to recursively form combinations
    def generate_combinations(index):
        if index == len(numbers):
            return [[]]  # Base case: return empty combination

        current_number = abs(numbers[index])  # Get the absolute value
        # Get combinations for the rest of the list
        rest_combinations = generate_combinations(index + 1)

        # Combine current number with positive and negative possibilities
        result = []
        for combination in rest_combinations:
            result.append([current_number] + combination)  # Positive
            result.append([-current_number] + combination)  # Negative

        return result

    return generate_combinations(0)

# Example usage:
print(foo([-4]))          # Output: [[4], [-4]]
print(foo([1, 1]))       # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))      # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))   # Output: [[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1],
                         #          [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]]
