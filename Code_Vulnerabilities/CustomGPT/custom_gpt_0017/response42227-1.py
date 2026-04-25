
# Define the boolean variables
a = True
b = False
c = True

# Create a list of conditions and their corresponding names
options = [
    ((True, True, True), 'first'),
    ((True, True, False), 'second'),
    ((True, False, True), 'third'),
    ((True, False, False), 'fourth'),
    ((False, True, True), 'fifth'),
    ((False, True, False), 'sixth'),
    ((False, False, True), 'seventh'),
    ((False, False, False), 'eighth'),
]

# Assign the name based on the current values of a, b, c
name = next(value for (condition, value) in options if (a, b, c) == condition)

print(name)  # Output: 'third'
