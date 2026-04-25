
# Boolean variables
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

# Calculate the index based on the booleans
index = (not a) << 2 | (not b) << 1 | (not c)
name = names[index]

print(name)  # Output will be based on the boolean values
