
def foo(numbers):
    # Function to generate all combinations of positive and negative numbers
    def backtrack(index, current):
        # If we've processed all numbers, add the current combination to results
        if index == len(numbers):
            results.append(current)
            return

        # Include the positive version of the current number
        backtrack(index + 1, current + [abs(numbers[index])])

        # Include the negative version of the current number
        backtrack(index + 1, current + [-abs(numbers[index])])

    results = []
    backtrack(0, [])
    return results

# Example usage:
print(foo([-4]))           # [[4], [-4]]
print(foo([1, 1]))        # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))       # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))    # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
