
def foo(nums):
    def generate(current, index):
        if index == len(nums):
            result.append(current)
            return
        # Add positive version
        generate(current + [abs(nums[index])], index + 1)
        # Add negative version
        generate(current + [-abs(nums[index])], index + 1)

    result = []
    generate([], 0)
    return result

# Example usages:
print(foo([-4]))            # [[4], [-4]]
print(foo([1, 1]))         # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))        # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))     # [[1, -1, 1], [1, -1, -1], [-1, 1, 1], [-1, 1, -1], [1, 1, -1], [-1, -1, 1], [-1, -1, -1]]
