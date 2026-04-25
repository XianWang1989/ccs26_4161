
# Assume a, b, c are your boolean values
a = True
b = False
c = True

# Create a list of names corresponding to the different combinations of a, b, c
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

# Calculate the index which is the sum of a, b, c acting as boolean (True=1, False=0)
index = (a << 2) + (b << 1) + c

# Assign the name based on the calculated index
name = names[index]

print(name)
