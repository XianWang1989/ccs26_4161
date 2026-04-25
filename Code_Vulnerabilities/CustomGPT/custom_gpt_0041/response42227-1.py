
# Booleans
a = True  # Example values
b = False
c = True

# Mapping booleans to an index: (False, True) as binary values
index = (not a, not b, not c)  # This creates a tuple of binary values
index_value = index[0] * 4 + index[1] * 2 + index[2]  # Calculate the index

# Tuple of names corresponding to each combination
names = (
    'eighth',  # 0: (False, False, False)
    'seventh', # 1: (False, False, True)
    'sixth',   # 2: (False, True, False)
    'fifth',   # 3: (False, True, True)
    'fourth',  # 4: (True, False, False)
    'third',   # 5: (True, False, True)
    'second',  # 6: (True, True, False)
    'first'    # 7: (True, True, True)
)

# Set the name based on the calculated index
name = names[index_value]

print(name)  # Output will depend on the boolean values of a, b, c
