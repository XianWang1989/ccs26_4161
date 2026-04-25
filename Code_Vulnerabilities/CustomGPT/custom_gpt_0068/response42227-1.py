
# Define your boolean values
a = True  # Example value
b = False  # Example value
c = True  # Example value

# Create a tuple with names indexed by the binary representation of a,b,c
names = (
    'eighth',  # 000 -> (False, False, False)
    'seventh', # 001 -> (False, False, True)
    'sixth',   # 010 -> (False, True, False)
    'fifth',   # 011 -> (False, True, True)
    'fourth',  # 100 -> (True, False, False)
    'third',   # 101 -> (True, False, True)
    'second',  # 110 -> (True, True, False)
    'first'    # 111 -> (True, True, True)
)

# Calculate the index based on boolean values
index = (not a) * 4 + (not b) * 2 + (not c) * 1

# Get the name based on index
name = names[index]

print(name)  # Outputs: 'third' if a=True, b=False, c=True
