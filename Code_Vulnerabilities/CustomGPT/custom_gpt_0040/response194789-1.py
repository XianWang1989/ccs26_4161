
def foo(numbers):
    # Helper function to generate combinations
    def generate_combinations(current, index):
        if index == len(numbers):
            result.append(current)
            return

        # Get the absolute value of the current number
        num = abs(numbers[index])

        # Include the positive and negative combinations
        generate_combinations(current + [num], index + 1)  # Positive
        generate_combinations(current + [-num], index + 1)  # Negative

    result = []
    generate_combinations([], 0)
    return result

# Test cases
print(foo([-4]))                      # Output: [[4], [-4]]
print(foo([1, 1]))                   # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))                  # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))                # Output: [[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1],
                                      #          [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]]
