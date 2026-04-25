
l1 = [4, 6, 8]
l2 = ['a', 'b', 'c']  # Note: 'a', 'b', and 'c' should be strings

# Join the lists element-wise using zip and convert it to a list of tuples
result = list(zip(l1, l2))

print(result)  # Output: [(4, 'a'), (6, 'b'), (8, 'c')]
