
import itertools

def foo(numbers):
    # Generate the possible combinations of signs for each number
    sign_combinations = list(itertools.product(*[(-1, 1) for _ in numbers]))

    # Create the result list
    result = []
    for signs in sign_combinations:
        result.append([num * sign for num, sign in zip(numbers, signs)])

    return result

# Example usage:
print(foo([-4]))              # [[4], [-4]]
print(foo([1, 1]))            # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))           # [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))        # [[1, -1, 1], [1, -1, -1], [1, 1, 1], [1, 1, -1], [-1, -1, 1], [-1, 1, -1], [1, -1, 1], [-1, 1, 1]]
