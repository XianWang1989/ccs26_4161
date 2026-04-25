
# Define your boolean variables
a = True
b = False
c = True

# Create a list where the index corresponds to the boolean values
options = [
    'eighth',  # 0: not a, not b, not c
    'seventh', # 1: not a, not b, c
    'sixth',   # 2: not a, b, not c
    'fifth',   # 3: not a, b, c
    'fourth',  # 4: a, not b, not c
    'third',   # 5: a, not b, c
    'second',  # 6: a, b, not c
    'first'    # 7: a, b, c
]

# Calculate the index
index = (not a) * 4 + (not b) * 2 + (not c)

# Get the name based on the index
name = options[index]

print(name)
