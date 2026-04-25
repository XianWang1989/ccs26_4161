
# Define the booleans
a = True
b = False
c = True

# Create a list of names corresponding to the boolean combinations
names = [
    'eighth', # not a, not b, not c
    'seventh', # not a, not b, c
    'sixth', # not a, b, not c
    'fifth', # not a, b, c
    'fourth', # a, not b, not c
    'third', # a, not b, c
    'second', # a, b, not c
    'first'   # a, b, c
]

# Create a list of booleans in the order of combinations
bool_combination = (not a, not b, not c)

# Calculate the index based on boolean values (maps booleans to indices)
index = int(bool_combination[0] * 4 + bool_combination[1] * 2 + bool_combination[2] * 1)

# Assign the name based on the calculated index
name = names[7 - index]  # Reverse the index for correct mapping

print(name)  # Output will depend on the values of a, b, c
