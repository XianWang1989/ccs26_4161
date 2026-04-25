
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Example phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define the grammar with cascading chunks
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}               # Media noun phrase
    RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}      # Relations with optional NP
    ENTITY: {<NN.*>}                         # Entities
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Print the chunked result
print(chunked)

# Draw the chunked tree (optional)
chunked.draw()
