
def foo(numbers):
    # Helper function to generate combinations
    def generate_combinations(nums, index):
        # Base case: if we've processed all numbers
        if index == len(nums):
            return [[]]  # Return empty list when no more numbers to process

        # Get the combinations from the rest of the numbers
        current_num = abs(nums[index])  # Use the absolute value for combinations
        combinations = generate_combinations(nums, index + 1)
        result = []

        # Build the new combinations with positive and negative values
        for combo in combinations:
            result.append([current_num] + combo)  # Positive
            result.append([-current_num] + combo)  # Negative

        return result

    return generate_combinations(numbers, 0)

# Test cases
print(foo([-4]))  # Output: [[4], [-4]]
print(foo([1, 1]))  # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))  # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))  # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
