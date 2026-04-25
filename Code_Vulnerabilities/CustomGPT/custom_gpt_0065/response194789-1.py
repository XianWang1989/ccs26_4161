
def foo(numbers):
    from itertools import product

    # Generate possibilities with '+' and '-'
    possibilities = list(product(*[(abs(num), -abs(num)) for num in numbers]))

    # Convert tuples to lists
    return [list(possibility) for possibility in possibilities]

# Example usages:
print(foo([-4]))                # [[4], [-4]]
print(foo([1, 1]))              # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))             # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))          # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [1, 1, 1], [-1, 1, 1], [-1, 1, -1]]
