
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}    # Including verbs here
    ENTITY: {<NN.*>}
"""

# To match specific words, you can include an optional branch
SPECIFIC_VERBS = r"{<VB.?>|<VB.*>}"
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}
    RELATION: {<VB.?>|<VB.*>}{<DT>?<JJ>*<NN.*>+}
    ENTITY: {<NN.*>}
"""
