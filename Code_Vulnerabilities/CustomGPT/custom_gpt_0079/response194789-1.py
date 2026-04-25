
import itertools

def foo(lst):
    # Generate a list of tuples with '+' and '-' variations
    options = []
    for num in lst:
        if num < 0:
            options.append([-abs(num), abs(num)])  # Add negative and positive
        else:
            options.append([abs(num), -abs(num)])  # Add positive and negative

    # Use itertools.product to generate all combinations
    combinations = list(itertools.product(*options))

    return [list(combination) for combination in combinations]

# Example usage
print(foo([-4]))              # [[4], [-4]]
print(foo([1, 2]))           # [[1, 2], [1, -2], [-1, 2], [-1, -2]]
print(foo([-1, 3]))          # [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -2, 3]))       # [[1, -2, 3], [1, -2, -3], [1, 2, 3], [1, 2, -3], [-1, -2, 3], [-1, -2, -3], [-1, 2, 3], [-1, 2, -3]]
