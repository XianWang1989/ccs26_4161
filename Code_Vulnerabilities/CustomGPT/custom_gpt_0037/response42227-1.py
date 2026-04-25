
def get_name(a, b, c):
    names = (
        'eighth',  # 0, 0, 0
        'seventh', # 0, 0, 1
        'sixth',   # 0, 1, 0
        'fifth',   # 0, 1, 1
        'fourth',  # 1, 0, 0
        'third',   # 1, 0, 1
        'second',  # 1, 1, 0
        'first'    # 1, 1, 1
    )

    index = (not a, not b, not c)  # Convert boolean values to indices
    return names[index[0] * 4 + index[1] * 2 + index[2]]  # Calculate index

# Example usage:
a, b, c = True, False, True
name = get_name(a, b, c)
print(name)  # Output: 'third'
