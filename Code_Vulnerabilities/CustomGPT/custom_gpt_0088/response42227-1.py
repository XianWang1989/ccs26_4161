
# Booleans
a = True
b = False
c = True

# Create a mapping of the state to names
states = (
    'eighth',   # 000
    'seventh',  # 001
    'sixth',    # 010
    'fifth',    # 011
    'fourth',   # 100
    'third',    # 101
    'second',   # 110
    'first'     # 111
)

# Use a binary representation to index into the states
index = (not a) << 2 | (not b) << 1 | (not c)
name = states[index]

print(name)
