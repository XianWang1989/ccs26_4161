
def generate(n):
    if n == 0:
        return [[]]  # Base case: return empty list for 0 length
    else:
        previous_combinations = generate(n - 1)
        # Generate current combinations by appending 0 and 1
        return [combination + [0] for combination in previous_combinations] + \
               [combination + [1] for combination in previous_combinations]

# Example usage
print(generate(4))
