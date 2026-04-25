
def foo(lst):
    # Helper function to generate combinations
    def generate_combinations(index, current):
        if index == len(lst):
            result.append(current)
            return

        # Handle the current number
        number = abs(lst[index])
        generate_combinations(index + 1, current + [number])  # Positive
        generate_combinations(index + 1, current + [-number])  # Negative

    result = []
    generate_combinations(0, [])
    return result

# Examples
print(foo([-4]))               # [[4], [-4]]
print(foo([1, 1]))             # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))            # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))         # [[1, 1, -1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1], [1, 1, 1], [-1, 1, 1], [1, -1, 1], [-1, -1, 1]]
