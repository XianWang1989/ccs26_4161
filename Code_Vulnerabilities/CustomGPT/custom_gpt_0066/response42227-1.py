
# Define the boolean values
a = True
b = False
c = True

# Create a list of names corresponding to the boolean combinations
names = ['eighth', 'seventh', 'sixth', 'fifth', 'fourth', 'third', 'second', 'first']

# Calculate the index based on the boolean values
index = (not a) * 4 + (not b) * 2 + (not c)

# Assign the name based on the calculated index
name = names[index]

print(name)  # Output will depend on the values of a, b, and c
