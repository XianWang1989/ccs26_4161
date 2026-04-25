
def foo(lst):
    # Helper function to generate combinations
    def backtrack(index, path):
        if index == len(lst):
            result.append(path)
            return
        # Generating positive and negative possibilities
        backtrack(index + 1, path + [abs(lst[index])])  # positive case
        backtrack(index + 1, path + [-abs(lst[index])])  # negative case

    result = []
    backtrack(0, [])
    return result

# Example usage:
print(foo([-4]))               # [[4], [-4]]
print(foo([1, 1]))            # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))           # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))        # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
