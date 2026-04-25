
# Boolean values
a, b, c = True, False, True  # set your boolean values here

# Mapping states to names using a tuple
names = (
    'eighth',  # 0, 0, 0
    'seventh', # 0, 0, 1
    'sixth',   # 0, 1, 0
    'fifth',   # 0, 1, 1
    'fourth',  # 1, 0, 0
    'third',   # 1, 0, 1
    'second',  # 1, 1, 0
    'first'    # 1, 1, 1
)

# Calculate the index
index = (not a) * 4 + (not b) * 2 + (not c) * 1

# Assign name based on the index
name = names[index]

print(name)
