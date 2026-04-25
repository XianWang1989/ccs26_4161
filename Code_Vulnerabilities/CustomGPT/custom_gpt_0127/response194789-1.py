
def foo(lst):
    # Base case: if the list is empty, return a list with an empty list
    if not lst:
        return [[]]

    # Get the first element and the rest of the list
    first = lst[0]
    rest = lst[1:]

    # Generate combinations for the rest of the list
    rest_combinations = foo(rest)

    # Create new combinations including the positive and negative of the first element
    current_combinations = []
    for combination in rest_combinations:
        current_combinations.append([abs(first)] + combination)  # Positive
        current_combinations.append([-abs(first)] + combination)  # Negative

    return current_combinations

# Examples
print(foo([-4]))                      # [[4], [-4]]
print(foo([1, 1]))                    # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))                   # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))                # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [-1, 1, 1], [-1, 1, -1], [1, 1, 1]]
