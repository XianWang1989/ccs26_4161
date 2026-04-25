
# Example boolean values
a = True
b = False
c = True

# Create a mapping of names using tuples
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

# Use the booleans as indices
index = (not a) * 4 + (not b) * 2 + (not c) * 1
name = names[index]

print(name)  # Output based on the boolean values
