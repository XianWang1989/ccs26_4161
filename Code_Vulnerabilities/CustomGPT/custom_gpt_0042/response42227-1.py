
# Boolean inputs
a = True
b = False
c = True

# Create a list of names
names = [
    'eighth',  # 000
    'seventh', # 001
    'sixth',   # 010
    'fifth',   # 011
    'fourth',  # 100
    'third',   # 101
    'second',  # 110
    'first'    # 111
]

# Convert booleans to an index value
index = (not a) << 2 | (not b) << 1 | (not c)

# Assign name based on the index
name = names[index]

print(name)  # Output will depend on the values of a, b, and c
