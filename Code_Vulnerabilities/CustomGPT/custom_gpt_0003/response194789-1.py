
def foo(numbers):
    def generate_combinations(index, current_combination):
        if index == len(numbers):
            results.append(current_combination)
            return

        # Add the positive version of the current number
        generate_combinations(index + 1, current_combination + [abs(numbers[index])])
        # Add the negative version of the current number
        generate_combinations(index + 1, current_combination + [-abs(numbers[index])])

    results = []
    generate_combinations(0, [])
    return results

# Test cases
print(foo([-4]))               # [[4], [-4]]
print(foo([1, 1]))            # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))           # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1]))           # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, -1, -1]))      # [[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1], [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]]
