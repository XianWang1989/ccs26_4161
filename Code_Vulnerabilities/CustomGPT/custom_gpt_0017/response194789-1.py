
def foo(lst):
    from itertools import product

    # Create a list of signs for each number in the input list
    signs = [[abs(num), -abs(num)] for num in lst]

    # Generate all combinations of the signs using product
    combinations = list(product(*signs))

    return combinations

# Example usage
print(foo([-4]))                # [[4], [-4]]
print(foo([1, 1]))              # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))             # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))          # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, 1], [1, 1, -1], [-1, 1, 1], [-1, 1, -1]]
