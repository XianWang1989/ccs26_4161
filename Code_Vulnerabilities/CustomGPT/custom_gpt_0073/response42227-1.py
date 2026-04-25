
# Define the boolean values
a, b, c = True, False, True  # example values

# Create a tuple of names corresponding to all possible combinations
names = (
    'eighth',   # 0: (False, False, False)
    'seventh',  # 1: (False, False, True)
    'sixth',    # 2: (False, True, False)
    'fifth',    # 3: (False, True, True)
    'fourth',   # 4: (True, False, False)
    'third',    # 5: (True, False, True)
    'second',   # 6: (True, True, False)
    'first'     # 7: (True, True, True)
)

# Calculate the index based on the boolean values
index = (a << 2) | (b << 1) | c  # Converts booleans to a single index
name = names[index]

print(name)  # Output the result
