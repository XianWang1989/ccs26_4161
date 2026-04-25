
import itertools

# List of numbers
numbers = [-4, -2, 1, 2, 5, 0]

# List comprehension using itertools.product
result = [(i, j, k) for i, j, k in itertools.product(numbers, repeat=3) if sum([i, j, k]) == 0]

# Output the result
print(result)
