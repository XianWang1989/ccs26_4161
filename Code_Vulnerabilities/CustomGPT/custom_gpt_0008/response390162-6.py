
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*>(<DT>?<JJ>*<NN.*>+)}  
  SPECIFIC_RELATION: {<VB.*>?<RB>?<VB.*>(<DT>?<JJ>*<NN.*>+)}  # Example for specific verbs
  ENTITY: {<NN.*>}
"""
