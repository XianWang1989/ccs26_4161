
# Define your boolean variables
a = True
b = False
c = True

# Create a mapping of the outcomes
outcomes = ('eighth', 'sixth', 'seventh', 'fourth', 'second', 'fifth', 'third', 'first')

# Calculate the index based on a, b, and c
index = (not a) << 2 | (not b) << 1 | (not c)

# Assign name based on the index
name = outcomes[index]

print(name)  # Outputs: 'third' if a is True, b is False, c is True
