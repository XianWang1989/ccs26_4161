
# Example boolean values
a = True
b = False
c = True

# Create a mapping of indices to names based on boolean values
index = (a << 2) | (b << 1) | c  # Binary representation of (a, b, c)
names = ('eighth', 'seventh', 'sixth', 'fifth', 'fourth', 'third', 'second', 'first')

# Assign name based on the index
name = names[index]

print(name)
