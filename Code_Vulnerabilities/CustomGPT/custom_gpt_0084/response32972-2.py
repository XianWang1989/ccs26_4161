
def generate_combinations(n):
    if n == 0:
        return [[]]
    else:
        smaller_combinations = generate_combinations(n - 1)
        return [comb + [0] for comb in smaller_combinations] + [comb + [1] for comb in smaller_combinations]

# Example usage
combinations = generate_combinations(4)
for combo in combinations:
    print(combo)
