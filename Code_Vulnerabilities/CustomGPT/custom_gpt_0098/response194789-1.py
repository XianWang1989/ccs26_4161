
def foo(nums):
    def backtrack(index, current):
        if index == len(nums):
            result.append(current[:])
            return
        current.append(abs(nums[index]))  # Add positive version
        backtrack(index + 1, current)
        current.pop()

        current.append(-abs(nums[index]))  # Add negative version
        backtrack(index + 1, current)
        current.pop()

    result = []
    backtrack(0, [])
    return result

# Example usage
print(foo([-4]))  # [[4], [-4]]
print(foo([1, 1]))  # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))  # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))  # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, 1], [1, 1, -1]]
