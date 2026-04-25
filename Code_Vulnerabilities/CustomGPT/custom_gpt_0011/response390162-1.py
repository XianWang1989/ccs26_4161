
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Define your grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                 # Chunk sequences of DT, JJ, NN (MEDIA)
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}        # Chunk verbs followed by MEDIA (RELATION)
    ENTITY: {<NN.*>}                           # Chunk single nouns (ENTITY)
"""

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Initialize the chunk parser with the specified grammar
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
chunked = chunk_parser.parse(tagged)

# Show the chunked structure
print(chunked)

# You can also visualize the chunk structure in a tree format
chunked.draw()
