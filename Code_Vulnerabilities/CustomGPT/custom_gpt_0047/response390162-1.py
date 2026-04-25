
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                  # Media phrases
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}          # Relations with verbs followed by media
  ENTITY: {<NN.*>}                             # Entities (single nouns)
"""
