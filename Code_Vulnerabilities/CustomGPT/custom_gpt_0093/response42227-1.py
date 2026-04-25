
def get_name(a, b, c):
    conditions = (
        (a, b, c, 'first'),
        (a, b, not c, 'second'),
        (a, not b, c, 'third'),
        (a, not b, not c, 'fourth'),
        (not a, b, c, 'fifth'),
        (not a, b, not c, 'sixth'),
        (not a, not b, c, 'seventh'),
        (not a, not b, not c, 'eighth'),
    )

    for condition in conditions:
        if condition[:3] == (a, b, c):
            return condition[3]

# Example usage:
a, b, c = True, False, True
name = get_name(a, b, c)
print(name)  # Output: 'third'
