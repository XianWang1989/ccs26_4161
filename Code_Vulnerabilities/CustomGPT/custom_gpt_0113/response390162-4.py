
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<VB.*|directed|acted><DT>?<JJ>*<NN.*>+}  # Include specific verbs
    ENTITY: {<NN.*>+}
"""
