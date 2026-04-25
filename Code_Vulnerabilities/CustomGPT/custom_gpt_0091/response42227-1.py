
# Assuming a, b, c are your boolean variables
a, b, c = True, False, True  # Example values

name = (
    'eighth',  # 0: (False, False, False)
    'sixth',   # 1: (False, False, True)
    'fifth',   # 2: (False, True, False)
    'first',   # 3: (True, True, False)
    'second',  # 4: (True, True, True)
    'fourth',  # 5: (True, False, True)
    'third',   # 6: (False, True, True)
)[(not a << 2) | (not b << 1) | not c]

print(name)
