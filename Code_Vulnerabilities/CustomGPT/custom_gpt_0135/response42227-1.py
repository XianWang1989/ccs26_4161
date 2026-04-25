
# Define the boolean values
a = True
b = False
c = True

# Create a tuple with the outcomes based on the boolean combinations
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

# Get the index based on the boolean values
index = (not a) * 4 + (not b) * 2 + (not c)
name = names[index]

print(name)
