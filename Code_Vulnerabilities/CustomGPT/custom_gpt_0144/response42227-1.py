# Define the options in binary order
options = [
    'eighth',  # 000
    'seventh', # 001
    'sixth',   # 010
    'fifth',   # 011
    'fourth',  # 100
    'third',   # 101
    'second',  # 110
    'first'    # 111
]

# Convert booleans to an integer index
index = (a << 2) | (b << 1) | c

# Get the corresponding name
name = options[index]
