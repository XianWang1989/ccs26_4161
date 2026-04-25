
a, b, c = True, False, True  # Example boolean values
name = (
    ('first', a and b and c),
    ('second', a and b and not c),
    ('third', a and not b and c),
    ('fourth', a and not b and not c),
    ('fifth', not a and b and c),
    ('sixth', not a and b and not c),
    ('seventh', not a and not b and c),
    ('eighth', not a and not b and not c)
)

name = next(name_value for name_value, condition in name if condition)
print(name)
