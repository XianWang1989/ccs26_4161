
def foo(numbers):
    def generate_combinations(index):
        if index == len(numbers):
            return [[]]  # Base case: return a list with an empty list

        current_number = abs(numbers[index])
        combinations = generate_combinations(index + 1)
        result = []

        for combo in combinations:
            result.append([current_number] + combo)   # Positive case
            result.append([-current_number] + combo)  # Negative case

        return result

    return generate_combinations(0)

# Examples
print(foo([-4]))              # [[4], [-4]]
print(foo([1, 1]))            # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))           # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))        # [[1, 1, 1], [1, -1, 1], [-1, 1, 1], [-1, -1, 1], [1, 1, -1], [1, -1, -1], [-1, 1, -1], [-1, -1, -1]]
