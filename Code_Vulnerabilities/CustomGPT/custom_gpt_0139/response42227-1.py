
# Define boolean values
a = True
b = False
c = True

# Create a mapping of outcomes based on the combinations of the booleans
name_options = [
    'eighth',  # (False, False, False)
    'seventh', # (False, False, True)
    'sixth',   # (False, True, False)
    'fifth',   # (False, True, True)
    'fourth',  # (True, False, False)
    'third',   # (True, False, True)
    'second',  # (True, True, False)
    'first'    # (True, True, True)
]

# Use the combination of a, b, c to compute the index
# a, b, c correspond to their respective binary values
index = (not a) * 4 + (not b) * 2 + (not c) * 1
name = name_options[index]

print(name)  # Output will be 'third' in case of a=True, b=False, c=True
