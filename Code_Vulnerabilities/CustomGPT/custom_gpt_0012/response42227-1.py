
# Boolean values
a = True
b = False
c = True

# Mapping based on boolean values
name = ('eighth', 'seventh', 'sixth', 'fifth', 'fourth', 'third', 'second', 'first')[
    (not a) * 4 + (not b) * 2 + (not c)
]

print(name)
