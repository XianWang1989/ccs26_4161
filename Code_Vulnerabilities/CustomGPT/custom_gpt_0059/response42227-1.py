
# Boolean values
a = True
b = False
c = True

# Define a list of names based on the combination of boolean values
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

# Calculate the index using bitwise operations
index = (a << 2) | (b << 1) | c

# Assign the name based on the calculated index
name = names[index]

print(name)
