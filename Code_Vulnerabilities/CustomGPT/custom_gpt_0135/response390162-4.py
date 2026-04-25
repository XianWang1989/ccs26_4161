
grammar = r"""
MEDIA: {<DT>?<JJ>*<NN.*>+}
RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}  # General relations
DIRECTED: {<VB.*><DT>?<JJ>*<NN.*>+}  # Modify this to target specific verbs if needed
ENTITY: {<NN.*>}
"""

# You can gather specific word checks with additional filtering
for subtree in chunks.subtrees():
    if subtree.label() == "RELATION":
        if 'directed' in [word for word, tag in subtree.leaves()]:
            print("Found directed relation:", subtree)
