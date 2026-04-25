
List1 = [[u'Case1', u'DP1', u'Configuration1', u'New'], 
          [u'Case2', u'DP2', u'Configuration2', u'New']]
List2 = [[u'DP1', u'EB1', u'Typ1'], 
          [u'DP2', u'EB2', u'Type2'], 
          [u'DP3', u'EB3', u'Type2']]

for key, item in enumerate(List2):
    # Find the matching item in List1
    matches = [x for x in List1 if (x[1] == item[0] and x[2] == 'Configuration1')]
    # Set the second element, if a match is found, otherwise set it to None
    List2[key] = [item[0], matches[0][3] if matches else None]

print(List2)  # Output: [[u'DP1', u'New'], [u'DP2', None], [u'DP3', None]]
