
def get_name(a, b, c):
    options = [
        (a, b, c, 'first'),
        (a, b, not c, 'second'),
        (a, not b, c, 'third'),
        (a, not b, not c, 'fourth'),
        (not a, b, c, 'fifth'),
        (not a, b, not c, 'sixth'),
        (not a, not b, c, 'seventh'),
        (not a, not b, not c, 'eighth')
    ]
    return next(name for a_val, b_val, c_val, name in options if a_val and b_val and c_val)

# Example usage
a, b, c = True, False, True
name = get_name(a, b, c)
print(name)  # Output: 'third'
