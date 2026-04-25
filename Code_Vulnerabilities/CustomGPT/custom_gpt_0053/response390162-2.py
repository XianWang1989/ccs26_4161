
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*>{<DT>?<JJ>*<NN.*>+} | {<VBZ|VBD|VBG|VBN|VBP> directed|acted} <DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
"""
