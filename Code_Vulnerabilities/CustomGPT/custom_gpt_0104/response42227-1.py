
# Define the boolean variables
a = True
b = False
c = True

# Create a mapping based on the binary values of a, b, c
name_mapping = (
    'eighth',  # 000
    'seventh', # 001
    'sixth',   # 010
    'fifth',   # 011
    'fourth',  # 100
    'third',   # 101
    'second',  # 110
    'first'    # 111
)

# Calculate the index by treating a, b, c as binary digits
index = (not a) * 4 + (not b) * 2 + (not c) * 1

# Retrieve the corresponding name from the mapping
name = name_mapping[index]

print(name)  # Output will be 'third' based on the above boolean values
