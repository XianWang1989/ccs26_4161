
a = True  # Example value
b = False  # Example value
c = True  # Example value

# Define the mapping in a tuple
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

# Calculate the index based on the truth values of a, b, and c
index = (not a) * 4 + (not b) * 2 + (not c) * 1
name = names[index]

print(name)
