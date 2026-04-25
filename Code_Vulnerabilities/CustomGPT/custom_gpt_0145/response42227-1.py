
# Define the three boolean variables
a = True
b = False
c = True

# Create a tuple that maps each combination of boolean values to the corresponding name
names = (
    'eighth',  # 000
    'seventh', # 001 (not a, not b, c)
    'sixth',   # 010 (not a, b, not c)
    'fifth',   # 011 (not a, b, c)
    'fourth',  # 100 (a, not b, not c)
    'third',   # 101 (a, not b, c)
    'second',  # 110 (a, b, not c)
    'first'    # 111 (a, b, c)
)

# Calculate the index based on the boolean values
index = (not a) << 2 | (not b) << 1 | (not c)

# Assign the name using the calculated index
name = names[index]

print(name)
