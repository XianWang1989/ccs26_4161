
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the input
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define your chunk grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                # Media noun phrases
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}        # Relations with verbs
    ENTITY: {<NN.*>}                          # Entity recognition
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged)

# Visualize the chunked output
print(chunked)

# Optionally, you can traverse the tree for specific chunks
for subtree in chunked.subtrees():
    if subtree.label() == 'MEDIA':
        print('Found MEDIA:', ' '.join(word for word, _ in subtree.leaves()))
    elif subtree.label() == 'RELATION':
        print('Found RELATION:', ' '.join(word for word, _ in subtree.leaves()))
    elif subtree.label() == 'ENTITY':
        print('Found ENTITY:', ' '.join(word for word, _ in subtree.leaves()))
