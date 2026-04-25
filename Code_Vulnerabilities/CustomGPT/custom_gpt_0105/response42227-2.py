
def get_name(a, b, c):
    names = [
        'eighth',  # 000
        'seventh', # 001
        'sixth',   # 010
        'fifth',   # 011
        'fourth',  # 100
        'third',   # 101
        'second',  # 110
        'first'    # 111
    ]
    index = (a << 2) | (b << 1) | c  # Create a binary index
    return names[index]

# Example usage
a, b, c = True, False, True
name = get_name(a, b, c)
print(name)  # Output: third
