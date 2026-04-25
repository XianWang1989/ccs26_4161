
# Tuple representing the names based on the boolean inputs
names = (
    'eighth',  # (0, 0, 0)
    'seventh', # (0, 0, 1)
    'sixth',   # (0, 1, 0)
    'fifth',   # (0, 1, 1)
    'fourth',  # (1, 0, 0)
    'third',   # (1, 0, 1)
    'second',  # (1, 1, 0)
    'first'    # (1, 1, 1)
)

# Calculate the index based on boolean values
index = (not a) * 4 + (not b) * 2 + (not c) * 1

# Assign the name based on the index
name = names[index]

# Example usage
a, b, c = True, False, True  # Change these values as needed
print(name)  # Output will be based on the values of a, b, and c
