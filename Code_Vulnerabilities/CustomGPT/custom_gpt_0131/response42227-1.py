
# Assuming a, b, and c are the boolean variables
a, b, c = True, False, True  # Example boolean values

# Convert boolean values to an integer: a is 4, b is 2, c is 1
index = (a << 2) | (b << 1) | c  # This creates a unique index for each combination

# List of names corresponding to each index
names = [
    'eighth',  # 000 (0)
    'seventh', # 001 (1)
    'sixth',   # 010 (2)
    'fifth',   # 011 (3)
    'fourth',  # 100 (4)
    'third',   # 101 (5)
    'second',  # 110 (6)
    'first'    # 111 (7)
]

# Retrieve the name based on the computed index
name = names[index]
print(name)
