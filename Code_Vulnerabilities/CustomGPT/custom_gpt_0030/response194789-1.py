
def foo(numbers):
    # Helper function to generate combinations
    def generate_combinations(index, current):
        if index == len(numbers):
            combinations.append(current)
            return

        # Include positive version
        generate_combinations(index + 1, current + [abs(numbers[index])])
        # Include negative version
        generate_combinations(index + 1, current + [-abs(numbers[index])])

    combinations = []
    generate_combinations(0, [])
    return combinations

# Example usage
print(foo([-4]))           # [[4], [-4]]
print(foo([1, 1]))        # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))       # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))    # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], 
                                        # [1, 1, 1], [1, 1, -1], [-1, 1, 1], [-1, 1, -1]]
