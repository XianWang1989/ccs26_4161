
List1 = [[u'Case1', u'DP1', u'Configuration1', u'New'], [u'Case2', u'DP2', u'Configuration2', u'New']]
List2 = [[u'DP1', u'EB1', u'Typ1'], [u'DP2', u'EB2', u'Type2'], [u'DP3', u'EB3', u'Type2']]

for key, item in enumerate(List2):
    # Find the relevant item in List1
    result = [x for x in List1 if (x[1] == item[0] and x[2] == 'Configuration1')]

    # Get the desired value or None if not found
    value = result[0][3] if result else None

    # Update List2 with the new value
    List2[key] = [item[0], value]

print(List2)
