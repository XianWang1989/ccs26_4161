
# Example of including specific words
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*|directed|acted><DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
  """
