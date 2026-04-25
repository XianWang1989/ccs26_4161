
List1 = [['Case1', 'DP1', 'Configuration1', 'New'], ['Case2', 'DP2', 'Configuration2', 'New']]
List2 = [['DP1', 'EB1', 'Typ1'], ['DP2', 'EB2', 'Type2'], ['DP3', 'EB3', 'Type2']]

for key, item in enumerate(List2):
    # Use a list comprehension and handle the case where no matches are found
    matching_items = [x for x in List1 if x[1] == item[0] and x[2] == 'Configuration1']

    # Check if we found any matching items
    if matching_items:
        List2[key] = [item[0], matching_items[0][3]]
    else:
        List2[key] = [item[0], None]

print(List2)
