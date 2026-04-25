
# Assuming a, b, and c are your boolean variables
a = True
b = False
c = True

# Create a tuple of names
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

# Calculate the index based on boolean values
index = (not a) * 4 + (not b) * 2 + (not c) * 1

# Assign the name based on the calculated index
name = names[index]

print(name)  # Output will be based on the boolean values of a, b, c
