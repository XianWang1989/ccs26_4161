
# Assuming a, b, and c are your boolean variables
a = True
b = False
c = True

# Create a tuple where the index is determined by the boolean values
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

# Use the tuple to assign name based on the boolean values
index = (not a) * 4 + (not b) * 2 + (not c) * 1
name = names[index]

print(name)  # Output will depend on the values of a, b, and c
