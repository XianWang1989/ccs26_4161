
# Boolean variables
a = True  # example value
b = False # example value
c = True  # example value

# Define a list of names based on the combinations of boolean values
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

# Combine the boolean values into a single index
index = (not a) << 2 | (not b) << 1 | (not c)

# Get the name based on the index
name = names[index]

print(name)
