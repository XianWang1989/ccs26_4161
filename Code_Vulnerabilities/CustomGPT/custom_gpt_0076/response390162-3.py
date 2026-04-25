
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                                   # Media NPs
  RELATION: {<VB.*|<VBZ|VBD|VBG>><DT>?<JJ>*<NN.*>+}          # Relations followed by NPs
  ENTITY: {<NN.*>}                                           # Entities
  """

# Adjust for specific words in the RELATION rule
specific_relation = r"""
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+|<VB.*> "directed"|<VB.*> "acted"}
"""

# Merge specific relations into the main grammar
combined_grammar = grammar + specific_relation
