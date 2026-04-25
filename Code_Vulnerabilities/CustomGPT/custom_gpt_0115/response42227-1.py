
# Boolean variables
a = True
b = False
c = True

# Create a mapping of the boolean combinations
name = [
    'eighth',  # 000
    'seventh', # 001
    'sixth',   # 010
    'fifth',   # 011
    'fourth',  # 100
    'third',   # 101
    'second',  # 110
    'first'    # 111
][a << 2 | b << 1 | c]

print(name)  # Output based on the values of a, b, c
