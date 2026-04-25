
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<VB.*>(<IN>|<VBD>|<VBN>)?<DT>?<JJ>*<NN.*>+}  # Including specific verbs
    ENTITY: {<NN.*>}
"""
