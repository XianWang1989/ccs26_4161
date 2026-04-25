
def get_name(a, b, c):
    index = (a << 2) | (b << 1) | c  # Create a binary index
    names = [
        'eighth', 'seventh', 'sixth', 'fifth',
        'fourth', 'third', 'second', 'first'
    ]
    return names[index]

# Example usage
a, b, c = True, False, True
name = get_name(a, b, c)
print(name)  # Output: third
