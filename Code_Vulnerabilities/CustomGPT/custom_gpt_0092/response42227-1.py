
# Define the boolean values
a = True    # Example value for a
b = False   # Example value for b
c = True    # Example value for c

# Create a tuple with the names
names = (
    'eighth',  # 0: (False, False, False)
    'seventh', # 1: (False, False, True)
    'sixth',   # 2: (False, True, False)
    'fifth',   # 3: (False, True, True)
    'fourth',  # 4: (True, False, False)
    'third',   # 5: (True, False, True)
    'second',  # 6: (True, True, False)
    'first'    # 7: (True, True, True)
)

# Calculate the index based on boolean values
index = (not a) * 4 + (not b) * 2 + (not c) * 1

# Use the index to get the name
name = names[index]

print(name)
