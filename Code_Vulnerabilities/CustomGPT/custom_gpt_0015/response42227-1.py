
def get_name(a, b, c):
    conditions = [
        (a, b, c, 'first'),
        (a, b, not c, 'second'),
        (a, not b, c, 'third'),
        (a, not b, not c, 'fourth'),
        (not a, b, c, 'fifth'),
        (not a, b, not c, 'sixth'),
        (not a, not b, c, 'seventh'),
        (not a, not b, not c, 'eighth')
    ]

    for a_val, b_val, c_val, name in conditions:
        if a_val and b_val and c_val:
            return name

# Example usage
a = True
b = False
c = True
result = get_name(a, b, c)
print(result)  # Outputs: 'third'
