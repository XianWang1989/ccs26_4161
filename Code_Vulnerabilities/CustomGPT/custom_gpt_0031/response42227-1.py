
# Define your boolean variables
a = True
b = False
c = True

# Create a tuple of the names corresponding to the combinations
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

# Calculate the index based on a, b, c
index = (not a) * 4 + (not b) * 2 + (not c)

# Assign the name based on the index
name = names[index]

print(name)
