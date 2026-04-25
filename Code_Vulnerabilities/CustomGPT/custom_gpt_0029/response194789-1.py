
def foo(numbers):
    def helper(index):
        if index == len(numbers):
            return [[]]  # base case: return a list containing an empty list

        num = abs(numbers[index])  # take the absolute value
        # Recur for the next index
        combinations = helper(index + 1)

        # Create new lists by adding both positive and negative versions of the current number
        result = []
        for comb in combinations:
            result.append([num] + comb)    # Positive
            result.append([-num] + comb)   # Negative

        return result

    return helper(0)

# Example usage:
print(foo([-4]))          # [[4], [-4]]
print(foo([1, 1]))       # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))      # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))   # [[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1], [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]]
