
from itertools import product

def foo(numbers):
    # Create a list of tuples with positive and negative forms of each number
    choices = []
    for num in numbers:
        if num > 0:
            choices.append((num, -num))
        elif num < 0:
            choices.append((-num, num))
        else:
            choices.append((0, 0))  # Still handle zero if you want

    # Generate the Cartesian product of the choices
    all_combinations = list(product(*choices))

    return all_combinations

# Test cases
print(foo([-4]))          # [[4], [-4]]
print(foo([1, 2]))       # [[1, 2], [1, -2], [-1, 2], [-1, -2]]
print(foo([-1, 3]))      # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1]))      # [[1, -1], [1, 1], [-1, -1], [-1, 1]]
print(foo([1, -1, 2]))   # [[1, -1, 2], [1, -1, -2], [1, 1, 2], ...]
