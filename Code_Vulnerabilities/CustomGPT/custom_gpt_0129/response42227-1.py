
# booleans a, b, and c
a = True
b = False
c = True

# Create a tuple where the index corresponds to the True/False values
# The index is calculated as `4*a + 2*b + c`, which gives us a unique index for each combination
name = (
    'eighth',    # 000: not a, not b, not c (8)
    'seventh',   # 001: not a, not b, c       (7)
    'sixth',     # 010: not a, b, not c      (6)
    'fifth',     # 011: not a, b, c          (5)
    'fourth',    # 100: a, not b, not c      (4)
    'third',     # 101: a, not b, c          (3)
    'second',    # 110: a, b, not c          (2)
    'first'      # 111: a, b, c              (1)
)[4 * a + 2 * b + c]

print(name)  # Output based on the values of a, b, and c
