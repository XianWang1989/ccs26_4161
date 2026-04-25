
def foo(nums):
    def generate_combinations(current, index):
        if index == len(nums):
            result.append(current)
            return

        # Get the absolute value of the current number
        num = abs(nums[index])
        # Generate combinations for positive and negative
        generate_combinations(current + [num], index + 1)  # Positive
        generate_combinations(current + [-num], index + 1) # Negative

    result = []
    generate_combinations([], 0)
    return result

# Example usage:
print(foo([-4]))  # Output: [[4], [-4]]
print(foo([1, 1]))  # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))  # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))  # Output: [[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1], [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]]
