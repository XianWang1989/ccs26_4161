
# Boolean values
a = True
b = False
c = True

# Tuple representing the states
states = (
    'eighth',    # 0, 0, 0
    'seventh',   # 0, 0, 1
    'sixth',     # 0, 1, 0
    'fifth',     # 0, 1, 1
    'fourth',    # 1, 0, 0
    'third',     # 1, 0, 1
    'second',    # 1, 1, 0
    'first'      # 1, 1, 1
)

# Indexing the states based on the boolean values
index = (not a) * 4 + (not b) * 2 + (not c)
name = states[index]

print(name)
