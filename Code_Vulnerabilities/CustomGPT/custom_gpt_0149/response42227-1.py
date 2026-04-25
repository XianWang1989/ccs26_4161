
# Define the names based on the boolean values
names = (
    'eighth',  # 0, 0, 0
    'seventh', # 0, 0, 1
    'sixth',   # 0, 1, 0
    'fifth',   # 0, 1, 1
    'fourth',  # 1, 0, 0
    'third',   # 1, 0, 1
    'second',  # 1, 1, 0
    'first'    # 1, 1, 1
)

# Indexing based on the boolean values
name = names[(not a) * 4 + (not b) * 2 + c]
