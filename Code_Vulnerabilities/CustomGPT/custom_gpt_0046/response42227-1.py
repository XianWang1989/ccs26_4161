
def get_name(a, b, c):
    options = (
        'eighth',   # 0b000
        'seventh',  # 0b001
        'sixth',    # 0b010
        'fifth',    # 0b011
        'fourth',   # 0b100
        'third',    # 0b101
        'second',   # 0b110
        'first'     # 0b111
    )
    index = (not a) + (not b * 2) + (not c * 4)
    return options[index]

# Example usage:
a, b, c = True, False, True
name = get_name(a, b, c)
print(name)  # Output: 'third'
