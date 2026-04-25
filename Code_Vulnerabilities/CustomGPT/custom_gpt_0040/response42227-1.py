
# Define the booleans
a = True
b = False
c = True

# Create a tuple with the names corresponding to the boolean combinations
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

# Use the boolean values as indices
index = (not a) * 4 + (not b) * 2 + (not c) * 1
name = names[index]

print(name)
