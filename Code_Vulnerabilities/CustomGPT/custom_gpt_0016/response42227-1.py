
# Define your boolean variables
a = True
b = False
c = True

# Create a list of conditions and corresponding names
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

# Use next to find the first true condition, defaulting to 'unknown' if none match
name = next((value for condition, value in conditions if condition), 'unknown')

print(name)  # Output: 'third'
