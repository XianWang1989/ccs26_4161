
def foo(nums):
    result = []

    def generate_combinations(index, current):
        if index == len(nums):
            result.append(current)
            return

        # Get the absolute value of the current number
        num = abs(nums[index])

        # Generate combinations for both positive and negative
        generate_combinations(index + 1, current + [num])
        generate_combinations(index + 1, current + [-num])

    generate_combinations(0, [])
    return result

# Examples
print(foo([-4]))              # [[4], [-4]]
print(foo([1, 1]))           # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))          # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))       # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
