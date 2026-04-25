
# Define your boolean values
a = True
b = False
c = True

# Create a lookup table based on the booleans
lookup = (
    'eighth',  # 0b000
    'seventh', # 0b001
    'sixth',   # 0b010
    'fifth',   # 0b011
    'fourth',  # 0b100
    'third',   # 0b101
    'second',  # 0b110
    'first'    # 0b111
)

# Calculate the index using the boolean values
index = (not a) << 2 | (not b) << 1 | (not c)
name = lookup[index]

print(name)
