
# Define the grammar with specific relation verbs
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB(?:.*|PP)?><DT>?<JJ>*<NN.*>+}  # Include any verb, but can be specific
  ENTITY: {<NN.*>}
"""

# For specific verbs, manually iterate
for subtree in result.subtrees():
    if subtree.label() == "RELATION":
        if subtree[0][0] in ["directed", "acted"]:
            print("Found specific relation:", subtree)
