
from itertools import product

def foo(numbers):
    possibilities = []
    for combo in product(*[[abs(num), -abs(num)] for num in numbers]):
        possibilities.append(list(combo))
    return possibilities

# Example usage
print(foo([-4]))            # [[4], [-4]]
print(foo([1, 1]))          # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))         # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))      # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [1, 1, 1], [-1, 1, 1], [-1, 1, -1]]
