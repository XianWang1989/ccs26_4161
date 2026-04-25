
def foo(lst):
    from itertools import product

    # Create a list of signs for each number
    signs = [[abs(num), -abs(num)] for num in lst]

    # Generate all combinations of signs using product
    possibilities = list(product(*signs))

    return possibilities

# Example usages
print(foo([-4]))            # [[4], [-4]]
print(foo([1, 1]))         # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))        # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))     # [[1, -1, 1], [-1, -1, 1], [1, 1, 1], [-1, 1, 1]]
