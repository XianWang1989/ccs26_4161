
# Define your boolean values
a = True  # Example value
b = False  # Example value
c = True  # Example value

# Use a tuple to represent the names based on bitwise combination of the booleans
names = (
    'eighth',  # 0b000: (False, False, False)
    'seventh',  # 0b001: (False, False, True)
    'sixth',    # 0b010: (False, True, False)
    'fifth',    # 0b011: (False, True, True)
    'fourth',   # 0b100: (True, False, False)
    'third',    # 0b101: (True, False, True)
    'second',   # 0b110: (True, True, False)
    'first'     # 0b111: (True, True, True)
)

# Create an index based on the boolean values
index = (not a) * 4 + (not b) * 2 + (not c)

# Assign name based on the index
name = names[index]

print(name)
