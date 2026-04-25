
# Define your boolean values
a = True  # Example values
b = False
c = True

# Create a tuple where the index corresponds to the binary representation of the booleans
name_options = (
    'eighth',  # 000
    'seventh', # 001
    'sixth',   # 010
    'fifth',   # 011
    'fourth',  # 100
    'third',   # 101
    'second',  # 110
    'first'    # 111
)

# Calculate the index based on the boolean values
index = (not a) << 2 | (not b) << 1 | (not c)

# Assign the name using the index
name = name_options[index]

print(name)
