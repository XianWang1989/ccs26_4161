
# Including specific verbs in the RELATION rule
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*>(directed|acted)<DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
"""
