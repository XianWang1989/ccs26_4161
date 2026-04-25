
a = True  # example boolean values
b = False
c = True

# Create a mapping of names based on the index of the boolean values
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
index = (not a) << 2 | (not b) << 1 | (not c)

# Assign the name based on the calculated index
name = names[index]

print(name)  # Output will be based on the values of a, b, and c
