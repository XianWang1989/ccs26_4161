
from itertools import product

# Define the list
nums = [-4, -2, 1, 2, 5, 0]

# Use product to create tuples and filter them based on the sum condition
result = [(i, j, k) for i, j, k in product(nums, repeat=3) if sum([i, j, k]) == 0]

# Output the result
print(result)
