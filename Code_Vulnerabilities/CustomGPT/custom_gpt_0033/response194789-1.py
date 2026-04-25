
from itertools import product

def foo(lst):
    # Create a list of tuples where each number has a positive and negative possibility
    possibilities = [(abs(num), -abs(num)) for num in lst]

    # Generate the Cartesian product of the possibilities
    combinations = product(*possibilities)

    # Convert tuples into lists
    return [list(combo) for combo in combinations]

# Example usage:
print(foo([-4]))
print(foo([1, 3]))
print(foo([1, -1, 3]))
