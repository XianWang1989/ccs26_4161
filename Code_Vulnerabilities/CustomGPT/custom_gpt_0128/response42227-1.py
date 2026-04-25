
# Boolean values
a = True
b = False
c = True

# Define conditions and corresponding names
conditions = [
    (a and b and c, 'first'),
    (a and b and not c, 'second'),
    (a and not b and c, 'third'),
    (a and not b and not c, 'fourth'),
    (not a and b and c, 'fifth'),
    (not a and b and not c, 'sixth'),
    (not a and not b and c, 'seventh'),
    (not a and not b and not c, 'eighth'),
]

# Find the corresponding name
name = next(name for condition, name in conditions if condition)

print(name)  # Output: 'third'
