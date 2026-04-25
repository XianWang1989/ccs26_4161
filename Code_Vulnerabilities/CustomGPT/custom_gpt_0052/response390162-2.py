
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB(?:Z|N|D|G|P|L|R|T|S|W)(?:\b|$)>|<VB.*><DT>?<JJ>*<NN.*>+} # Including specific verbs
  ENTITY: {<NN.*>}
"""
