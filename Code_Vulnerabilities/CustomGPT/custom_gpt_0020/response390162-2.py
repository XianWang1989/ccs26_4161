
if subtree.label() == 'RELATION':
    if any(word in ["directed", "acted"] for word, pos in subtree.leaves()):
        print("Found RELATION with specific verb:", " ".join(word for word, pos in subtree.leaves()))
