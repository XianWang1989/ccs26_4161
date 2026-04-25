
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*>(<DT>?<JJ>*<NN.*>+|<NNP>+)}  # NNP for proper nouns
  ENTITY: {<NN.*>}
  DIRECTED_OR_ACTED: {<VB.?> <DT>?<JJ>*<NN.*>+}  # Example for specific verbs
"""
