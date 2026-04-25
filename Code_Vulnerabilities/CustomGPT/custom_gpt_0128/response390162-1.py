
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                 # Chunk for media entities
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}        # Chunk for relationships 
  ENTITY: {<NN.*>}                            # Chunk for entities
"""
