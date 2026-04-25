
# Boolean variables
a = True
b = False
c = True

# Create a tuple of outcomes
outcomes = (
    'eighth',   # 000
    'seventh',  # 001
    'sixth',    # 010
    'fifth',    # 011
    'fourth',   # 100
    'third',    # 101
    'second',   # 110
    'first'     # 111
)

# Calculate index
index = (not a) * 4 + (not b) * 2 + (not c) * 1

# Assign name based on the calculated index
name = outcomes[index]

print(name)
