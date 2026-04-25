
# Define the boolean values
a = True
b = False
c = True

# Create a list of names, where the index corresponds to the boolean values
names = [
    'eighth',  # 000
    'seventh',  # 001
    'sixth',    # 010
    'fifth',    # 011
    'fourth',   # 100
    'third',    # 101
    'second',   # 110
    'first'     # 111
]

# Calculate the index based on the booleans
index = (not a) * 4 + (not b) * 2 + (not c) * 1

# Assign the name based on the calculated index
name = names[index]

print(name)
