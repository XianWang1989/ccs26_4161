
import itertools

def foo(nums):
    possibilities = []
    for signs in itertools.product(*[('+', '-') for _ in nums]):
        current_combination = [0] * len(nums)
        for i, sign in enumerate(signs):
            current_combination[i] = abs(nums[i]) if sign == '+' else -abs(nums[i])
        possibilities.append(current_combination)
    return possibilities

# Test cases
print(foo([-4]))            # [[4], [-4]]
print(foo([1, 1]))          # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))         # [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))      # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, 1], [1, 1, -1], [-1, 1, 1], [-1, 1, -1]]
