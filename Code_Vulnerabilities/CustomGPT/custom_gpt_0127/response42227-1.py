
# Define your boolean values
a = True
b = False
c = True

# Create a mapping using a tuple of names
names = (
    'eighth',  # 0: (False, False, False)
    'seventh', # 1: (False, False, True)
    'sixth',   # 2: (False, True, False)
    'fifth',   # 3: (False, True, True)
    'fourth',  # 4: (True, False, False)
    'third',   # 5: (True, False, True)
    'second',  # 6: (True, True, False)
    'first',   # 7: (True, True, True)
)

# Determine the index based on boolean values
index = (not a) * 4 + (not b) * 2 + (not c)

# Assign the name based on the index
name = names[index]

print(name)
