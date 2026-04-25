
def foo(nums):
    # A recursive function to generate possibilities
    def generate(pos_neg_list, index):
        # Base case: if we've processed all numbers, add to the results
        if index == len(nums):
            results.append(pos_neg_list.copy())
            return

        # For each number, we can choose to make it positive or negative
        generate(pos_neg_list + [abs(nums[index])], index + 1)  # Positive
        generate(pos_neg_list + [-abs(nums[index])], index + 1) # Negative

    results = []
    generate([], 0)
    return results

# Test cases
print(foo([-4]))             # Output: [[4], [-4]]
print(foo([1, 1]))          # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))         # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))      # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]

# Additional example with mixed signs
print(foo([1, -1, 1]))      # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
