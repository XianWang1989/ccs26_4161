
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+|<VB.*>(directed|acted)<DT>?<JJ>*<NN.*>}
  ENTITY: {<NN.*>}
"""
