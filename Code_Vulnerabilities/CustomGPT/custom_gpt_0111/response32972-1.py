
def generate(n):
    if n == 0:
        return [[]]
    else:
        combinations = generate(n - 1)
        return [combo + [0] for combo in combinations] + [combo + [1] for combo in combinations]

print(generate(4))
