
def get_name(a, b, c):
    # Create a tuple with all possible results indexed by the boolean values
    options = (
        'eighth',  # 000
        'seventh', # 001
        'sixth',   # 010
        'fifth',   # 011
        'fourth',  # 100
        'third',   # 101
        'second',  # 110
        'first'    # 111
    )

    # Calculate the index based on the boolean values
    index = (not a) << 2 | (not b) << 1 | (not c)

    return options[index]

# Example usage
a, b, c = True, False, True
name = get_name(a, b, c)
print(name)  # Output: 'third'
