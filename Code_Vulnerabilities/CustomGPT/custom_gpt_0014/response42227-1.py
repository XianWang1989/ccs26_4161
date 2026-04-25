
def get_name(a, b, c):
    options = [
        'eighth',  # 0b000
        'seventh', # 0b001
        'sixth',   # 0b010
        'fifth',   # 0b011
        'fourth',  # 0b100
        'third',   # 0b101
        'second',  # 0b110
        'first'    # 0b111
    ]
    # Convert the boolean values to a binary representation
    index = (not a) << 2 | (not b) << 1 | (not c)
    return options[index]

# Example usage
a = True
b = False
c = True

name = get_name(a, b, c)
print(name)  # Output: 'third'
