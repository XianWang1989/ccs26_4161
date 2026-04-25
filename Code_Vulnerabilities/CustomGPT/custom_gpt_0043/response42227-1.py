
# Boolean variables
a = True
b = False
c = True

# Create a tuple of names corresponding to each combination of a, b, and c
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

# Index calculation based on the boolean values
index = (not a) * 4 + (not b) * 2 + (not c) * 1

# Get the corresponding name
name = names[index]

print(name)
