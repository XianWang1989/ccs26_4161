
# Define the boolean variables
a = True
b = False
c = True

# Tuple of possible names based on the combination of boolean values
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

# Calculate index based on boolean values
index = (not a << 2) | (not b << 1) | (not c)
name = names[index]

print(name)  # Output: 'third'
