
def foo(lst):
    if not lst:
        return [[]]  # Base case: return a list with an empty list

    first = lst[0]  # Get the first element
    rest = lst[1:]  # Get the rest of the list

    # Recursive call to generate combinations of the rest of the list
    combinations = foo(rest)

    # Create new combinations with the current number as positive and negative
    results = []
    for combo in combinations:
        results.append([abs(first)] + combo)    # Add positive
        results.append([-abs(first)] + combo)   # Add negative

    return results

# Test cases
print(foo([-4]))           # [[4], [-4]]
print(foo([1, 1]))        # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))       # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))    # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], ...]

