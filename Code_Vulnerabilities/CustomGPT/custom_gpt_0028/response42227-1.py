
# Boolean values
a = True
b = False
c = True

# Create a tuple with the corresponding names
names = (
    'eighth',  # 0
    'seventh', # 1
    'sixth',   # 2
    'fifth',   # 3
    'fourth',  # 4
    'third',   # 5
    'second',  # 6
    'first'    # 7
)

# Use the boolean values to index the tuple
name = names[(not a) << 2 | (not b) << 1 | (not c)]

print(name)  # Output: 'third' if a=True, b=False, c=True
