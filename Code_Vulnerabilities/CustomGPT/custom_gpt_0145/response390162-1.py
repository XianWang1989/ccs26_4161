
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase to chunk
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig directed by someone"

# Tokenization and POS tagging
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define your grammar for cascading chunking
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                      # Media entities
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}              # Relations with optional determinants
    ENTITY: {<NN.*>}                                # General entities
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
chunked = chunk_parser.parse(tagged)

# Print out the chunked result
print(chunked)

# Visualizing the parsed tree
chunked.draw()
