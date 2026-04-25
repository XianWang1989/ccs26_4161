
# Tuples for names based on boolean values
names = (
    'eighth',  # 0, 0, 0
    'seventh', # 0, 0, 1
    'sixth',   # 0, 1, 0
    'fifth',   # 0, 1, 1
    'fourth',  # 1, 0, 0
    'third',   # 1, 0, 1
    'second',  # 1, 1, 0
    'first'    # 1, 1, 1
)

# Combine boolean values into an index for the names tuple
index = (not a) * 4 + (not b) * 2 + (not c) * 1

# Assign name based on the computed index
name = names[index]

# Example boolean values
a, b, c = True, True, False
print(name)  # Output: second
