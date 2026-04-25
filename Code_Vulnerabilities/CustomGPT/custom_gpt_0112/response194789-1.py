
import itertools

def foo(numbers):
    # Generate all combinations of positive and negative for each number
    possibilities = list(itertools.product(*[(abs(n), -abs(n)) for n in numbers]))
    return possibilities

# Example usages:
print(foo([-4]))            # [[4], [-4]]
print(foo([1, 1]))          # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))         # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))      # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], 
                             #  [1, 1, -1], [1, 1, 1], [-1, 1, -1], [-1, 1, 1]]
