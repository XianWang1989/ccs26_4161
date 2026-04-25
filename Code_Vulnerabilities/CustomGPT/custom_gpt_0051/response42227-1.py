
# Boolean variables
a = True
b = False
c = True

# Tuple of possible names
names = (
    'eighth',  # 0: not a, not b, not c
    'seventh', # 1: not a, not b, c
    'sixth',   # 2: not a, b, not c
    'fifth',   # 3: not a, b, c
    'fourth',  # 4: a, not b, not c
    'third',   # 5: a, not b, c
    'second',  # 6: a, b, not c
    'first'    # 7: a, b, c
)

# Calculate index based on boolean values
index = (not a) * 4 + (not b) * 2 + (not c)
name = names[index]

print(name)
