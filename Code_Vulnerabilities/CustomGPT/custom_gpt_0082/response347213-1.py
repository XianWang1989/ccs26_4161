
List1 = [[u'Case1', u'DP1', u'Configuration1', u'New'], [u'Case2', u'DP2', u'Configuration2', u'New']]
List2 = [[u'DP1', u'EB1', u'Typ1'], [u'DP2', u'EB2', u'Type2'], [u'DP3', u'EB3', u'Type2']]

# Use list comprehension with a safe access method
List2 = [
    [item[0], 
     ([x[3] for x in List1 if (x[1] == item[0] and x[2] == 'Configuration1')] or [None])[0]]
    for item in List2
]

print(List2)
