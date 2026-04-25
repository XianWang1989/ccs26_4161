
def generate_combinations(n):
    if n == 0:
        return [[]]
    else:
        smaller_combinations = generate_combinations(n - 1)
        return [combo + [0] for combo in smaller_combinations] + [combo + [1] for combo in smaller_combinations]

# Example usage
result = generate_combinations(4)
print(result)
