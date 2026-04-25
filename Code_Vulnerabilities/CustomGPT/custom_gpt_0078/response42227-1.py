
# Boolean variables
a = True
b = False
c = True

# Create a list of names corresponding to each combination
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

# Calculate index: (a << 2) + (b << 1) + c
index = (a << 2) + (b << 1) + c

# Assign name based on index
name = names[index]

print(name)
