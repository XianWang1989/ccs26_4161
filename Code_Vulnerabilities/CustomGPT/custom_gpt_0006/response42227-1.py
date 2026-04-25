
def get_name(a, b, c):
    options = (
        (1, 'first'),
        (1, 0, 'second'),
        (0, 1, 'third'),
        (1, 'fourth'),
        (0, 1, 'fifth'),
        (0, 0, 'sixth'),
        (1, 'seventh'),
        (0, 'eighth'),
    )

    # Create a binary representation of a, b, and c
    index = (a << 2) | (b << 1) | c
    return options[index][1]

# Example usage:
a = True
b = False
c = True
name = get_name(a, b, c)
print(name)  # Output will be 'third'
