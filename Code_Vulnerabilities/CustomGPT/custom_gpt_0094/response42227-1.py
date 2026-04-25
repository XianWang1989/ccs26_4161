
# Boolean variables
a = True
b = False
c = True

# Create a tuple of names
names = ('eighth', 'seventh', 'sixth', 'fifth', 'fourth', 'third', 'second', 'first')

# Calculate the index based on boolean values
index = (not a) * 4 + (not b) * 2 + (not c)

# Assign based on the calculated index
name = names[index]
print(name)
