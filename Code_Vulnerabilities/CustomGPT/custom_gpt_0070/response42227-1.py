
def determine_name(a, b, c):
    names = (
        'eighth',  # 000
        'seventh', # 001
        'sixth',   # 010
        'fifth',   # 011
        'fourth',  # 100
        'third',   # 101
        'second',  # 110
        'first'    # 111
    )

    index = (not a) << 2 | (not b) << 1 | (not c)
    return names[index]

# Example usage
a, b, c = True, False, True
name = determine_name(a, b, c)
print(name)  # Outputs: 'third'
