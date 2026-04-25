
# Define a tuple of names based on the boolean pattern
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

# Convert boolean values to an index for the tuple
index = (not a) * 4 + (not b) * 2 + (not c) * 1

# Assign the name based on the calculated index
name = name_options[index]
