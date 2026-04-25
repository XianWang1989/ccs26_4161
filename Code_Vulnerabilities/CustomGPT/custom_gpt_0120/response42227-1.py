
# Assuming a, b, and c are your boolean variables
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

# Create an index based on the boolean values
index = (not a) << 2 | (not b) << 1 | not c

# Assign the name based on the index
name = names[index]

print(name)
