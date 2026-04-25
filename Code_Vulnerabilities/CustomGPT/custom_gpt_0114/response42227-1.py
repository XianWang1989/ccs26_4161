
# Assume a, b, c are your boolean variables
a, b, c = True, False, True  # Example values

# Create a mapping of boolean combinations to names
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

# Use a tuple index based on the state of a, b, c
index = (not a) << 2 | (not b) << 1 | (not c)
name = names[index]

print(name)  # Output will depend on the values of a, b, c
