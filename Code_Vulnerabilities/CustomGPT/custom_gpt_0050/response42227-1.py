
# Boolean variables
a = True
b = False
c = True

# Tuple to map boolean combinations to names
names = (
    "eighth",  # 000
    "seventh", # 001
    "sixth",   # 010
    "fifth",   # 011
    "fourth",  # 100
    "third",   # 101
    "second",  # 110
    "first"    # 111
)

# Calculate the index based on the boolean values
index = (not a) * 4 + (not b) * 2 + (not c) * 1

# Assign name based on index
name = names[index]

print(name)
