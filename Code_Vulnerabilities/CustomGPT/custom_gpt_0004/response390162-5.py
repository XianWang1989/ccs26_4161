
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                                 # Media chunk
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+|<VB.?(directed|acted)>} # Relation chunk with specific verbs
  ENTITY: {<NN.*>}                                          # Entity chunk
"""
