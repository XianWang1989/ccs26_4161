
# Assuming a, b, c are your boolean variables
a, b, c = True, False, True  # Example values

# Create a list of names corresponding to each combination of (a, b, c)
names = [
    'eighth',  # (False, False, False) -> 0
    'seventh', # (False, False, True) -> 1
    'sixth',   # (False, True, False) -> 2
    'fifth',   # (False, True, True) -> 3
    'fourth',  # (True, False, False) -> 4
    'third',   # (True, False, True) -> 5
    'second',  # (True, True, False) -> 6
    'first'    # (True, True, True) -> 7
]

# Calculate index based on boolean values
index = (int(a) << 2) | (int(b) << 1) | int(c)
name = names[index]

print(name)  # Output based on the values of a, b, c
