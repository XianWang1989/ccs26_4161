from itertools import product

def foo(nums):
    # Handle special case where input uses + and - symbols
    if all(isinstance(n, str) and n in ('+', '-') for n in nums):
        nums = [1] * len(nums)  # Replace with placeholders since only signs matter

    # Create a list of tuples for each number: (abs(num), -abs(num))
    possibilities = [(abs(n), -abs(n)) for n in nums]
    
    # Generate the Cartesian product of all possibilities
    return [list(p) for p in product(*possibilities)]

# Examples:
print(foo([-4]))          # [[4], [-4]]
print(foo(['+', '+']))    # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo(['-', '+']))    # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))       # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo(['+', '-', '+']))  # 8 combinations
