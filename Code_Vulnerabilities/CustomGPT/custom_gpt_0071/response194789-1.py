
def foo(nums):
    def backtrack(index):
        if index == len(nums):
            result.append(current.copy())
            return

        # Choose the positive version
        current.append(abs(nums[index]))
        backtrack(index + 1)
        current.pop()

        # Choose the negative version
        current.append(-abs(nums[index]))
        backtrack(index + 1)
        current.pop()

    result = []
    current = []
    backtrack(0)
    return result

# Example usage
print(foo([-4]))                 # [[4], [-4]]
print(foo([1, 1]))               # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))              # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))           # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [-1, 1, 1], [1, 1, 1], [-1, -1, 1]]
