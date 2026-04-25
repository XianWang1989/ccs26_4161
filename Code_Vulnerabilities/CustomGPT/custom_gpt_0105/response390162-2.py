
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*>(<DT>?<JJ>*<NN.*>+|<VB.*>)}
  ENTITY: {<NN.*>}
"""

# Assuming you want to capture specific verbs:
# Create a custom rule for capturing specific words
special_verbs = r"<VB(?:Z|D|N|G)?|*|acted|directed>"

# Update grammar to check for these special verbs
grammar = grammar.replace('VB.*', special_verbs)
