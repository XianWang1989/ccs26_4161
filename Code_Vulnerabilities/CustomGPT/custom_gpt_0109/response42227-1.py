
# Boolean values
a = True
b = False
c = True

# Tuple of names based on combinations of a, b, c
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

# Use the binary representation of a, b, c as an index
index = (not a) << 2 | (not b) << 1 | (not c)
name = names[index]

print(name)
