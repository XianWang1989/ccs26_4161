
# Assume a, b, c are your boolean variables
a = True
b = False
c = True

# Create a tuple with the names in the order of their corresponding boolean combinations
names = (
    'eighth',  # 000 (False, False, False)
    'seventh', # 001 (False, False, True)
    'sixth',   # 010 (False, True, False)
    'fifth',   # 011 (False, True, True)
    'fourth',  # 100 (True, False, False)
    'third',   # 101 (True, False, True)
    'second',  # 110 (True, True, False)
    'first'    # 111 (True, True, True)
)

# Calculate the index based on the boolean values
index = (a << 2) | (b << 1) | c

# Assign the name based on the index
name = names[index]

print(name)  # Output: 'third'
