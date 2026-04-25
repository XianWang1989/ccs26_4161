
# Define the boolean variables
a = True
b = False
c = True

# Map the boolean values to the corresponding names
names = (
    'eighth',   # (False, False, False)
    'seventh',  # (False, False, True)
    'sixth',    # (False, True, False)
    'fifth',    # (False, True, True)
    'fourth',   # (True, False, False)
    'third',    # (True, False, True)
    'second',   # (True, True, False)
    'first'     # (True, True, True)
)

# Calculate the index by converting booleans to integers (0 or 1)
index = (not a) * 4 + (not b) * 2 + (not c)

# Assign the name based on the index
name = names[index]

print(name)
