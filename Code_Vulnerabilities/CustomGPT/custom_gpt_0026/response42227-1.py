
# Assuming a, b, and c are your boolean variables
a, b, c = True, False, True  # Example values

# Create a tuple of names
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

# Compute the index based on boolean values
index = (not a) * 1 + (not b) * 2 + (not c) * 4
name = names[index]

print(name)
