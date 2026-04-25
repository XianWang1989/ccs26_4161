
List1 = [[u'Case1', u'DP1', u'Configuration1', u'New'], 
          [u'Case2', u'DP2', u'Configuration2', u'New']]

List2 = [[u'DP1', u'EB1', u'Typ1'], 
          [u'DP2', u'EB2', u'Type2'], 
          [u'DP3', u'EB3', u'Type2']]

# Create the new combined list
for key, item in enumerate(List2):
    # Using a try-except block to handle possible IndexError
    try:
        matched_item = [x for x in List1 if (x[1] == item[0] and x[2] == 'Configuration1')]
        List2[key] = [item[0], matched_item[0][3]] if matched_item else [item[0], None]
    except IndexError:
        List2[key] = [item[0], None]

print(List2)
