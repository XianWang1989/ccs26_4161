
# Boolean values
a = True  # Example value
b = False # Example value
c = True  # Example value

# Tuple representing the names based on boolean combinations
names = (
    'eighth',  # 000
    'seventh', # 001
    'sixth',   # 010
    'fifth',   # 011
    'fourth',  # 100
    'third',   # 101
    'second',  # 110
    'first'    # 111
)

# Calculate index based on boolean values
index = (not a) << 2 | (not b) << 1 | (not c)

# Assign name based on index
name = names[index]

print(name)
