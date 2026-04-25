
def foo(lst):
    if not lst:
        return [[]]  # Base case: return a list with an empty list

    first = lst[0]
    rest = lst[1:]

    # Generate combinations for the rest of the list
    combinations = foo(rest)

    # Create new combinations by adding both positive and negative versions of the first element
    new_combinations = []
    for combo in combinations:
        new_combinations.append([abs(first)] + combo)  # Positive version
        new_combinations.append([-abs(first)] + combo)  # Negative version

    return new_combinations

# Example usage:
print(foo([-4]))
print(foo([1, 3]))
print(foo([1, -1, 1]))
