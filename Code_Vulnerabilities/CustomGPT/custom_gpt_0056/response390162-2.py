
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<V.*|directed|acted><DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
"""
