
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*>{<IN|directed|acted><DT>?<JJ>*<NN.*>+}}
  ENTITY: {<NN.*>}
"""
