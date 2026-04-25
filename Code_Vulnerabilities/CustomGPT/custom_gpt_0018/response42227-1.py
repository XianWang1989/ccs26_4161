
# Define the boolean values
a = True
b = False
c = True

# Create a tuple with the corresponding names
names = (
    'eighth',    # 0b000 (not a, not b, not c)
    'seventh',   # 0b001 (not a, not b, c)
    'sixth',     # 0b010 (not a, b, not c)
    'fifth',     # 0b011 (not a, b, c)
    'fourth',    # 0b100 (a, not b, not c)
    'third',     # 0b101 (a, not b, c)
    'second',    # 0b110 (a, b, not c)
    'first'      # 0b111 (a, b, c)
)

# Calculate the index based on the boolean values
index = (a << 2) | (b << 1) | c

# Assign the name based on the index
name = names[index]

print(name)  # Output: 'third'
