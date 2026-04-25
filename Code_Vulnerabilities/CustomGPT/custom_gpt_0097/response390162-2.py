
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<VB.*> <VB.*>|<VB.*> <DT>?<JJ>*<NN.*>+}
    ENTITY: {<NN.*>}
"""
