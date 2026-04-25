
import itertools

def foo(numbers):
    # Generate the combinations of positive and negative values
    possibilities = list(itertools.product(*[[abs(num), -abs(num)] for num in numbers]))
    return possibilities

# Example usage
print(foo([-4]))                # [[4], [-4]]
print(foo([1, 1]))              # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))            # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))          # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], ...]
