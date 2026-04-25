
# Assuming a, b, c are your boolean variables
a = True  # Example value
b = False  # Example value
c = True  # Example value

# Create a tuple of names based on the possible combinations of a, b, c
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

# Calculate the index using the boolean values
index = (not a) << 2 | (not b) << 1 | (not c)

# Assign the corresponding name
name = names[index]

print(name)
