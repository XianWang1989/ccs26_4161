
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                       # Media phrases
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}              # Relations like "directed" or "acted"
  ENTITY: {<NN.*>}                                 # Entities
"""
