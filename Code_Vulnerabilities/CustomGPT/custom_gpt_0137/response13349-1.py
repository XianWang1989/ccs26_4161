
l1 = [4, 6, 8]
l2 = ['a', 'b', 'c']

# Combining the lists element-wise
result = [(x, y) for x, y in zip(l1, l2)]

print(result)  # Output: [(4, 'a'), (6, 'b'), (8, 'c')]
