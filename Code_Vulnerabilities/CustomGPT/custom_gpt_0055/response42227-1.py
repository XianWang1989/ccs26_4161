
# Assuming a, b, c are your boolean variables
a, b, c = True, False, False  # Example values

# Create a tuple with the names based on the combinations of a, b, c
names = (
    'eighth',  # 0b000
    'seventh', # 0b001
    'sixth',   # 0b010
    'fifth',   # 0b011
    'fourth',  # 0b100
    'third',   # 0b101
    'second',  # 0b110
    'first'    # 0b111
)

# Calculate the index based on the boolean values
index = (not a << 2) | (not b << 1) | not c

# Assign the name based on the index
name = names[index]

print(name)  # Output: 'fourth'
