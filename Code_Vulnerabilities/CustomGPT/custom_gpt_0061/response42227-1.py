
# Boolean values
a = True
b = False
c = True

# Mapping names based on binary combinations of a, b, and c
name_mapping = [
    'eighth',  # 000
    'seventh', # 001
    'sixth',   # 010
    'fifth',   # 011
    'fourth',  # 100
    'third',   # 101
    'second',  # 110
    'first'    # 111
]

# Calculate the index based on boolean values
index = (not a) * 4 + (not b) * 2 + (not c) * 1

# Get the name using the calculated index
name = name_mapping[index]

print(name)
