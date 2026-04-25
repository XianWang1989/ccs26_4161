
def foo(numbers):
    def backtrack(index):
        if index == len(numbers):
            result.append(current.copy())
            return
        current.append(abs(numbers[index]))  # Add positive version
        backtrack(index + 1)
        current.pop()  # Backtrack
        current.append(-abs(numbers[index]))  # Add negative version
        backtrack(index + 1)
        current.pop()  # Backtrack

    result = []
    current = []
    backtrack(0)
    return result

# Example usage:
print(foo([-4]))            # Output: [[4], [-4]]
print(foo([1, 1]))         # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))        # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))     # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [1, 1, 1]]
