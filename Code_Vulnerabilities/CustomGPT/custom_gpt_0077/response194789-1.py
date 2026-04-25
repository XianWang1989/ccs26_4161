
import itertools

def foo(numbers):
    # Generate all combinations of '+' and '-'
    signs = list(itertools.product(*[(num, -num) for num in numbers]))
    # Create the list of lists for output
    result = [list(sign) for sign in signs]
    return result

# Example usage
print(foo([-4]))          # [[4], [-4]]
print(foo([1, 1]))       # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))      # [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))   # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1],
                          #  [1, 1, -1], [1, 1, 1], [-1, 1, 1], [-1, 1, -1]]

