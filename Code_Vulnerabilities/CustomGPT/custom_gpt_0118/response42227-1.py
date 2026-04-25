
def get_name(a, b, c):
    names = (
        'eighth',  # (False, False, False)
        'seventh', # (False, False, True)
        'sixth',   # (False, True, False)
        'fifth',   # (False, True, True)
        'fourth',  # (True, False, False)
        'third',   # (True, False, True)
        'second',  # (True, True, False)
        'first'    # (True, True, True)
    )

    # Convert booleans to indices (0 or 1)
    index = (not a) << 2 | (not b) << 1 | (not c)
    return names[index]

# Example usage
a, b, c = True, False, True
name = get_name(a, b, c)
print(name)  # Output: 'third'
