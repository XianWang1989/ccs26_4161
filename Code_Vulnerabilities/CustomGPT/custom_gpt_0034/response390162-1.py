
import nltk
from nltk import pos_tag
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by Daniel Craig"

# Tokenize the phrase
tokens = word_tokenize(phrase)

# POS tagging
tagged_tokens = pos_tag(tokens)

# Define the grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                         # Media entities
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}                 # Relations with nouns
    ENTITY: {<NN.*>}                                   # General entities
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunks = chunk_parser.parse(tagged_tokens)

# Display chunks
print(chunks)

# Draw the resulting chunk tree
chunks.draw()
