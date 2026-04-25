
def foo(numbers):
    def backtrack(index):
        if index == len(numbers):
            result.append(current.copy())
            return

        # Consider both positive and negative variants
        # Positive
        current.append(abs(numbers[index]))
        backtrack(index + 1)
        # Negative
        current.pop()  # Remove positive variant
        current.append(-abs(numbers[index]))
        backtrack(index + 1)
        current.pop()  # Remove negative variant

    result = []
    current = []
    backtrack(0)
    return result

# Test examples
print(foo([-4]))               # [[4], [-4]]
print(foo([1, 1]))             # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))            # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))         # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
print(foo([1, -1, -1]))        # [[1, 1, -1], [1, 1, -1], [-1, 1, -1], [-1, -1, -1]]
