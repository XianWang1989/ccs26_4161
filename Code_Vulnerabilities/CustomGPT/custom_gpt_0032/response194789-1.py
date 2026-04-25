
def foo(numbers):
    if not numbers:
        return [[]]  # Base case for recursion, return empty list

    # Recursive call to get combinations for the rest of the list
    rest_combinations = foo(numbers[1:])

    # Build new combinations with the current number as positive and negative
    current_number = abs(numbers[0])  # Get the absolute value
    combinations = []

    for combination in rest_combinations:
        combinations.append([current_number] + combination)  # Positive
        combinations.append([-current_number] + combination) # Negative

    return combinations

# Test cases
print(foo([-4]))            # [[4], [-4]]
print(foo([1, 1]))         # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))        # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))     # [[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1],
                           #  [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]]
