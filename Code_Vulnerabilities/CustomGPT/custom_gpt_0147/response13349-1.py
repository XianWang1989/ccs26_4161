
# Step 1: Define the lists
l1 = [4, 6, 8]
l2 = ['a', 'b', 'c']  # Note: wrap 'a', 'b', 'c' in quotes to make them string literals

# Step 2: Use zip function to combine lists element-wise
result = list(zip(l1, l2))

# Step 3: Print the result
print(result)  # Output: [(4, 'a'), (6, 'b'), (8, 'c')]
