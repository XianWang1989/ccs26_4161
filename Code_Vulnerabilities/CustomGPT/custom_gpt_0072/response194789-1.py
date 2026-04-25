
def foo(nums):
    def backtrack(current, index):
        if index == len(nums):
            result.append(current)
            return
        # Choose the positive version
        backtrack(current + [abs(nums[index])], index + 1)
        # Choose the negative version
        backtrack(current + [-abs(nums[index])], index + 1)

    result = []
    backtrack([], 0)
    return result

# Example usage
print(foo([-4]))
print(foo([1, 1]))
print(foo([-1, 3]))
print(foo([1, -1, 1]))
