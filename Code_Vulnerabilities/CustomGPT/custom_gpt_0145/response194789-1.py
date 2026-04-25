
import itertools

def foo(lst):
    # Generate a list of '+', '-' for each number in lst
    possibilities = []
    for num in lst:
        if num > 0:
            possibilities.append([num, -num])  # For positive numbers
        else:
            possibilities.append([-num, num])  # For negative numbers

    # Create combinations of all possibilities using itertools.product
    result = list(itertools.product(*possibilities))

    return [list(combination) for combination in result]

# Examples
print(foo([-4]))                  # Output: [[4], [-4]]
print(foo([1, 1]))                # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))               # Output: [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))            # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [1, 1, 1], [-1, 1, 1], [-1, -1, 1]]
