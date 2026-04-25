
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                    # Media chunk
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}           # Relation chunk
  ENTITY: {<NN.*>}                               # Entity chunk
"""
