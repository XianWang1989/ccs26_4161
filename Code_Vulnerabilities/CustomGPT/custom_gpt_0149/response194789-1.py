
def foo(arr):
    # Base case: if the array is empty, return an empty list inside a list
    if not arr:
        return [[]]

    # Recursive case: generate combinations for the rest of the list
    rest_combinations = foo(arr[1:])
    current_number = abs(arr[0])

    # Generate all combinations for the current number
    result = []
    for combination in rest_combinations:
        result.append([current_number] + combination)  # Positive
        result.append([-current_number] + combination) # Negative

    return result

# Example usage
print(foo([-4]))               # [[4], [-4]]
print(foo([1, 1]))            # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))           # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))        # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, 1], [1, 1, -1], [-1, 1, 1], [-1, 1, -1]]
