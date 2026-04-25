
# Assuming a, b, c are your boolean values
a = True
b = False
c = True

# Create a tuple of possible names
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
index = (not a) * 4 + (not b) * 2 + (not c) * 1

# Assign the name based on the index
name = names[index]

# Output the result
print(name)  # This will print 'third' based on the values of a, b, and c
