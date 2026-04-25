
# Assuming a, b, c are your boolean values
a, b, c = True, False, True  # Example values

# Create a list of names based on the combination of a, b, c
names = [
    'eighth',  # 000
    'seventh', # 001
    'sixth',   # 010
    'fifth',   # 011
    'fourth',  # 100
    'third',   # 101
    'second',  # 110
    'first'    # 111
]

# Calculate the index based on a, b, c
index = (not a) * 4 + (not b) * 2 + (not c) * 1
name = names[index]

print(name)
