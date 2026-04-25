
# Example boolean variables
a = True
b = False
c = True

# Define the mapping of names
names = (
    'eighth',  # 000
    'seventh', # 001
    'sixth',   # 010
    'fifth',   # 011
    'fourth',  # 100
    'third',   # 101
    'second',  # 110
    'first'    # 111
)

# Calculate the index from the boolean values
index = (not a) * 4 + (not b) * 2 + (not c)

# Assign the name based on the calculated index
name = names[index]

print(name)  # Output will be 'third' if a=True, b=False, c=True
