
def get_name(a, b, c):
    options = (
        ('first', a, b, c),
        ('second', a, b, not c),
        ('third', a, not b, c),
        ('fourth', a, not b, not c),
        ('fifth', not a, b, c),
        ('sixth', not a, b, not c),
        ('seventh', not a, not b, c),
        ('eighth', not a, not b, not c),
    )

    for name, *conditions in options:
        if all(conditions):
            return name

# Example usage
a, b, c = True, False, True
name = get_name(a, b, c)
print(name)  # Output: 'third'
