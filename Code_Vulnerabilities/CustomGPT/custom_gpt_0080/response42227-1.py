
def get_name(a, b, c):
    # Creating a tuple of possible outcomes based on boolean values
    outcomes = (
        ('first', a, b, c),
        ('second', a, b, not c),
        ('third', a, not b, c),
        ('fourth', a, not b, not c),
        ('fifth', not a, b, c),
        ('sixth', not a, b, not c),
        ('seventh', not a, not b, c),
        ('eighth', not a, not b, not c),
    )

    # Loop over outcomes and return the name that matches
    for name, condition_a, condition_b, condition_c in outcomes:
        if condition_a and condition_b and condition_c:
            return name

# Example usage
a = True
b = False
c = True
name = get_name(a, b, c)
print(name)  # Output: 'third'
