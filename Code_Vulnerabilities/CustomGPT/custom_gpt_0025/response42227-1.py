
def get_name(a, b, c):
    # Create a list of names corresponding to the boolean combination
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

    # Calculate the index (binary: a is leftmost, c is rightmost)
    index = (not a) << 2 | (not b) << 1 | (not c)

    # Return the corresponding name
    return names[index]

# Example usage
a, b, c = True, False, True
name = get_name(a, b, c)
print(name)  # Output: 'third'
