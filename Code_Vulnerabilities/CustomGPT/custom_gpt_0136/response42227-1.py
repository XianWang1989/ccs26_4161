
# Define boolean values
a = True
b = False
c = True

# Create a mapping of conditions to results
conditions = (
    (a, b, c),      # first
    (a, b, not c),  # second
    (a, not b, c),  # third
    (a, not b, not c),  # fourth
    (not a, b, c),  # fifth
    (not a, b, not c),  # sixth
    (not a, not b, c),  # seventh
    (not a, not b, not c)  # eighth
)

# Assign name based on truth values
name = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth'][conditions.index(True) for conditions if True in conditions]

print(name)
