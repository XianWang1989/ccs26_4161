
# Assuming a, b, c are your boolean variables
a = True  # Example values
b = False
c = True

# Create a tuple of names corresponding to the possible combinations
names = (
    'eighth',     # 0, 0, 0
    'seventh',    # 0, 0, 1
    'sixth',      # 0, 1, 0
    'fifth',      # 0, 1, 1
    'fourth',     # 1, 0, 0
    'third',      # 1, 0, 1
    'second',     # 1, 1, 0
    'first'       # 1, 1, 1
)

# Index into the tuple based on the boolean values
name = names[a << 2 | b << 1 | c]

print(name)  # Output will be based on the values of a, b, c
