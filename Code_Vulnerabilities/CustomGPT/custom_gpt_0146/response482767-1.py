
from itertools import product

# List of numbers
nums = [-4, -2, 1, 2, 5, 0]

# Using itertools.product for three-tuples
result = [
    (i, j, k) 
    for i, j, k in product(nums, repeat=3) 
    if sum([i, j, k]) == 0
]

# Output the result
print(result)
