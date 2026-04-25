
# Define the boolean values
a = True  # Example value
b = False  # Example value
c = True  # Example value

# List of names corresponding to different boolean combinations
names = (
    'eighth',  # 0, 0, 0
    'seventh',  # 0, 0, 1
    'sixth',    # 0, 1, 0
    'fifth',    # 0, 1, 1
    'fourth',   # 1, 0, 0
    'third',    # 1, 0, 1
    'second',   # 1, 1, 0
    'first'     # 1, 1, 1
)

# Calculate the index based on the boolean values
index = (not a) << 2 | (not b) << 1 | (not c)
name = names[index]

print(name)  # Outputs the corresponding name based on the boolean values
