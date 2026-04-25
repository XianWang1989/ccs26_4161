
# Define your boolean variables
a = True
b = False
c = True

# Create a tuple with names corresponding to the binary combinations.
names = (
    'eighth',   # 000 (False, False, False) -> index 0
    'seventh',  # 001 (False, False, True)  -> index 1
    'sixth',    # 010 (False, True, False)  -> index 2
    'fifth',    # 011 (False, True, True)   -> index 3
    'fourth',   # 100 (True, False, False)  -> index 4
    'third',    # 101 (True, False, True)   -> index 5
    'second',   # 110 (True, True, False)    -> index 6
    'first'     # 111 (True, True, True)     -> index 7
)

# Calculate the index based on the truth values of a, b, and c
index = (a << 2) | (b << 1) | c

# Assign the correct name using the calculated index
name = names[index]

print(name)  # Output: 'third'
