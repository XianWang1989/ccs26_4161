
List1 = [[u'Case1', u'DP1', u'Configuration1', u'New'], [u'Case2', u'DP2', u'Configuration2', u'New']]
List2 = [[u'DP1', u'EB1', u'Typ1'], [u'DP2', u'EB2', u'Type2'], [u'DP3', u'EB3', u'Type2']]

for key, item in enumerate(List2):
    # Find matches based on the condition
    matches = [x for x in List1 if (x[1] == item[0] and x[2] == 'Configuration1')]

    # Use a ternary operator to handle No matches case
    List2[key] = [item[0], matches[0][3] if matches else None]

print(List2)
