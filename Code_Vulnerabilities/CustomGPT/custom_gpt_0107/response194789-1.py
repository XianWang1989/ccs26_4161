
def foo(numbers):
    # Function to generate all combinations
    def backtrack(index, current):
        if index == len(numbers):
            result.append(current)
            return
        # Recursive calls for positive and negative options
        backtrack(index + 1, current + [abs(numbers[index])])  # Positive
        backtrack(index + 1, current + [-abs(numbers[index])])  # Negative

    result = []
    backtrack(0, [])
    return result

# Example usage
print(foo([-4]))           # [[4], [-4]]
print(foo([1, 2]))        # [[1, 2], [1, -2], [-1, 2], [-1, -2]]
print(foo([-1, 3]))       # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 2]))    # [[1, -1, 2], [1, -1, -2], [-1, -1, 2], [-1, -1, -2], ...]
