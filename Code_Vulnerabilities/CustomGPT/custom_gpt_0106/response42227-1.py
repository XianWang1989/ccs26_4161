
def get_name(a, b, c):
    # Create a list where the index corresponds to the boolean values
    names = [
        'eighth',  # (0, 0, 0)
        'seventh', # (0, 0, 1)
        'sixth',   # (0, 1, 0)
        'fifth',   # (0, 1, 1)
        'fourth',  # (1, 0, 0)
        'third',   # (1, 0, 1)
        'second',  # (1, 1, 0)
        'first'    # (1, 1, 1)
    ]

    # Calculate the index based on the boolean values
    index = (not a) * 4 + (not b) * 2 + (not c)
    return names[index]

# Example usage
a = True
b = False
c = True
name = get_name(a, b, c)
print(name)  # Output: 'third'
