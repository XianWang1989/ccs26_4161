
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

# Get index for name_options based on a, b, c
index = (not a) << 2 | (not b) << 1 | (not c)
name = name_options[index]
