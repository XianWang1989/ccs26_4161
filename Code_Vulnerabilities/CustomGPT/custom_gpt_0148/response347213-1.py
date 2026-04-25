
List1 = [[u'Case1', u'DP1', u'Configuration1', u'New'], [u'Case2', u'DP2', u'Configuration2', u'New']]
List2 = [[u'DP1', u'EB1', u'Typ1'], [u'DP2', u'EB2', u'Type2'], [u'DP3', u'EB3', u'Type2']]

for key, item in enumerate(List2):
    # Use a next with a default to avoid IndexError
    match = next((x for x in List1 if x[1] == item[0] and x[2] == 'Configuration1'), None)
    List2[key] = [item[0], match[3] if match else None]

print(List2)
