
# Assuming a, b, and c are your boolean variables
a = True
b = False
c = True

# Create a mapping of boolean states to names
name = (
    (a, b, c),
    (a, b, not c),
    (a, not b, c),
    (a, not b, not c),
    (not a, b, c),
    (not a, b, not c),
    (not a, not b, c),
    (not a, not b, not c)
)

# Define names corresponding to the boolean states
names = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth']

# Get the index of the matching tuple
index = name.index((a, b, c))

# Assign the name
result = names[index]

print(result)
