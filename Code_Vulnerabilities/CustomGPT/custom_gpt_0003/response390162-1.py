
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                 # Chunk sequences of DT, JJ, NN
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}        # Chunk verbs followed by optional DT, JJ, NN
  ENTITY: {<NN.*>}                           # Chunk singular nouns
"""
