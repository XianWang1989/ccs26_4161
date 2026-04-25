
def foo(numbers):
    # Base case: if the list is empty, return a list containing an empty list
    if not numbers:
        return [[]]

    # Recursive call for the rest of the list
    rest_combinations = foo(numbers[1:])

    # Build combinations for current number
    current_number = abs(numbers[0])
    current_combinations = []

    for combination in rest_combinations:
        current_combinations.append([current_number] + combination)  # Positive
        current_combinations.append([-current_number] + combination) # Negative

    return current_combinations

# Examples
print(foo([-4]))           # [[4], [-4]]
print(foo([1, 1]))        # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))       # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))    # [[1, 1, -1], [1, -1, -1], [-1, 1, 1], [-1, -1, 1], [-1, -1, -1]]
