
l1 = [4, 6, 8]
l2 = ['a', 'b', 'c']  # Ensure that 'a', 'b', 'c' are strings

# Using zip to join the lists element-wise
result = list(zip(l1, l2))

print(result)  # Output: [(4, 'a'), (6, 'b'), (8, 'c')]
