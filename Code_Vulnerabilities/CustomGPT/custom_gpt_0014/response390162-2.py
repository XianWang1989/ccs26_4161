
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*> | <VB.*>{<DT>?<JJ>*<NN.*>+} | <VB {<VB.*>+(directed|acted)}>
  ENTITY: {<NN.*>}
"""
