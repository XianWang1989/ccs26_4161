
from itertools import product

def foo(nums):
    # Generate the list of tuples with possible signs for each number
    possibilities = []
    for num in nums:
        possibilities.append((abs(num), -abs(num)))

    # Use product to create all combinations of signs
    combinations = list(product(*possibilities))

    # Convert each tuple to a list
    return [list(comb) for comb in combinations]

# Example usage:
print(foo([-4]))                # Output: [[4], [-4]]
print(foo([1, 1]))             # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))            # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))         # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], ...]
