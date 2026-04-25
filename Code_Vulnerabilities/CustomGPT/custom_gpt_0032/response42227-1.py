
# Booleans
a = True
b = False
c = True

# Create a tuple of names
names = (
    'eighth',    # 000
    'seventh',   # 001
    'sixth',     # 010
    'fifth',     # 011
    'fourth',    # 100
    'third',     # 101
    'second',    # 110
    'first'      # 111
)

# Calculate index based on boolean values
index = (not a) << 2 | (not b) << 1 | (not c)

# Get the name from the tuple
name = names[index]

print(name)  # Output will be 'third' if a=True, b=False, c=True
