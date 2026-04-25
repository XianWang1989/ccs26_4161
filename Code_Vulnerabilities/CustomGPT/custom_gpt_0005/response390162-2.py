
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<V.*><VB.*><DT>?<JJ>*<NN.*>}      # Adjusted to include specific verbs
    ENTITY: {<NN.*>}
"""
