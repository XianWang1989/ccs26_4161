
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define grammar for chunking
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}             # Chunk sequences of DT, JJ, and NN as MEDIA
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}    # Chunk verbs followed by NPs as RELATION
    ENTITY: {<NN.*>}                       # Chunk NN for ENTITY
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
chunked = chunk_parser.parse(tagged)

# Draw the resulting chunk tree
chunked.draw()

# Print out the chunks
for subtree in chunked.subtrees():
    if subtree.label() in ['MEDIA', 'RELATION', 'ENTITY']:
        print(subtree)
