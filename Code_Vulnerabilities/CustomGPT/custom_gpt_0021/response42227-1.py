
# Boolean variables
a = True
b = False
c = True

# Create a tuple where the index corresponds to the binary representation of a, b, c
# (0,0,0) corresponds to index 0, (1,0,0) to index 1, ..., (1,1,1) to index 7
name_map = (
    'eighth',  # 0: (False, False, False)
    'fourth',  # 1: (True,  False, False)
    'sixth',   # 2: (False, True,  False)
    'fifth',   # 3: (False, True,  True)
    'third',   # 4: (True,  False, True)
    'second',  # 5: (True,  True,  False)
    'first',   # 6: (True,  True,  True)
    # Optionally, return None or raise an error for invalid states
)

# Calculate index based on a, b, c
index = (a << 2) | (b << 1) | c  # a is the most significant bit

# Assign name based on the index
name = name_map[index]

print(name)  # Output: 'third'
