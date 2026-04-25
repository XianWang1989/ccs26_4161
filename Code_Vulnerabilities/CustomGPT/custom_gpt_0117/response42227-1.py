
# Example booleans
a = True
b = False
c = True

# Create a mapping of binary combinations to names
name_mapping = (
    'eighth',    # (0, 0, 0)
    'seventh',   # (0, 0, 1)
    'sixth',     # (0, 1, 0)
    'fifth',     # (0, 1, 1)
    'fourth',    # (1, 0, 0)
    'third',     # (1, 0, 1)
    'second',    # (1, 1, 0)
    'first'      # (1, 1, 1)
)

# Calculate the index based on the boolean values
index = (not a) * 4 + (not b) * 2 + (not c)

# Assign the name based on the index
name = name_mapping[index]

print(name)
