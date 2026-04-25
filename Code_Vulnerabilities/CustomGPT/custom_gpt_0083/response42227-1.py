
# Boolean variables
a = True  # Replace with your boolean value
b = False  # Replace with your boolean value
c = True  # Replace with your boolean value

# List of conditions and corresponding names
conditions = [
    (a, b, c, 'first'),
    (a, b, not c, 'second'),
    (a, not b, c, 'third'),
    (a, not b, not c, 'fourth'),
    (not a, b, c, 'fifth'),
    (not a, b, not c, 'sixth'),
    (not a, not b, c, 'seventh'),
    (not a, not b, not c, 'eighth')
]

# Determine the name based on the conditions
name = next(name for (x, y, z, name) in conditions if x and y and z)

print(name)
