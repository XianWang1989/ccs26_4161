
from itertools import product

def foo(numbers):
    # Create a list of possible signs for each number
    possibilities = []
    for num in numbers:
        if num > 0:  # Positive number
            possibilities.append([num, -num])
        elif num < 0:  # Negative number
            possibilities.append([-num, num])
        else:  # Zero case (if necessary)
            possibilities.append([0])  # Can customize this if needed

    # Generate all combinations using itertools.product
    all_combinations = list(product(*possibilities))

    return all_combinations

# Example usage
print(foo([-4]))              # [[4], [-4]]
print(foo([1, 1]))            # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))           # [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))        # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], ...]
print(foo([-1, 3]))           # [[-1, 3], [-1, -3], [1, 3], [1, -3]]
