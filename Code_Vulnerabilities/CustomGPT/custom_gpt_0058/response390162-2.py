
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}               
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+} | {<V.*> directed|acted}
    ENTITY: {<NN.*>}                        
"""
