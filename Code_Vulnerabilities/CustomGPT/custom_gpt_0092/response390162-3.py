
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*>(directed|acted|featuring)<DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
"""
