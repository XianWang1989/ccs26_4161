
def foo(nums):
    # Recursive helper function to generate combinations
    def backtrack(index, current):
        if index == len(nums):
            result.append(current)
            return
        # Explore both positive and negative possibilities
        backtrack(index + 1, current + [abs(nums[index])])  # Positive
        backtrack(index + 1, current + [-abs(nums[index])]) # Negative

    result = []
    backtrack(0, [])
    return result

# Testing the function with the provided examples
print(foo([-4]))           # [[4], [-4]]
print(foo([1, 1]))        # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))       # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))    # [[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1],
                           # [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]]
