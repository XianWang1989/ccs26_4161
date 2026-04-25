
# Sample boolean values
a = True
b = False
c = True

# List of names corresponding to the combinations of a, b, and c
names = [
    'eighth',   # 000: not a, not b, not c
    'seventh',  # 001: not a, not b, c
    'sixth',    # 010: not a, b, not c
    'fifth',    # 011: not a, b, c
    'fourth',   # 100: a, not b, not c
    'third',    # 101: a, not b, c
    'second',   # 110: a, b, not c
    'first'     # 111: a, b, c
]

# Calculate the index by converting boolean values to integers
index = (a << 2) | (b << 1) | c

# Get the name based on the index
name = names[index]

print(name)  # Output will be based on the values of a, b, and c
