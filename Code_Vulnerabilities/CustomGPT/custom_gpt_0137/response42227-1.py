
# Define the boolean variables
a = True
b = False
c = True

# Create a tuple with the names corresponding to the index generated from a, b, c
# Using (not a, not b, not c) will give us the indexes we need for the tuple.
names = (
    'eighth',    # (False, False, False)
    'seventh',   # (False, False, True)
    'sixth',     # (False, True, False)
    'fifth',     # (False, True, True)
    'fourth',    # (True, False, False)
    'third',     # (True, False, True)
    'second',    # (True, True, False)
    'first'      # (True, True, True)
)

# Calculate the index by using binary representation of the boolean values
# Map a, b, c to index: a * 4 + b * 2 + c * 1
index = (not a) * 4 + (not b) * 2 + (not c) * 1

# Get the name based on the index
name = names[index]

print(name)  # Output: 'third' (if a=True, b=False, c=True)
