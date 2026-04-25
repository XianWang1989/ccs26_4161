
# Define the boolean values
a = True
b = False
c = True

# Create a list of names corresponding to the possible combinations of a, b, c
names = [
    'eighth',   # (False, False, False)
    'seventh',  # (False, False, True)
    'sixth',    # (False, True, False)
    'fifth',    # (False, True, True)
    'fourth',   # (True, False, False)
    'third',    # (True, False, True)
    'second',   # (True, True, False)
    'first'     # (True, True, True)
]

# Convert booleans to index (0 or 1)
index = (not a) * 4 + (not b) * 2 + (not c)

# Assign the name based on the index
name = names[index]

print(name)
