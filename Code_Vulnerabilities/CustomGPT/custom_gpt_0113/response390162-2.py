
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                     # Chunk sequences of DT, JJ, NN
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}             # Verb followed by NP
    ENTITY: {<NN.*>+}                              # Chunk nouns
"""
