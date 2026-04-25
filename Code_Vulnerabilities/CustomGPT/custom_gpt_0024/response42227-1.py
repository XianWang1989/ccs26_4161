
# Define the booleans
a = True
b = False
c = True

# Use a tuple to map the combinations to the desired strings
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

# Calculate the index based on the boolean values
index = (not a) << 2 | (not b) << 1 | (not c)
name = names[index]

print(name)  # Outputs: 'third' in this example
