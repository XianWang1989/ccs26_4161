
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the phrase
tokens = word_tokenize(phrase)
tagged_tokens = pos_tag(tokens)

# Define the chunking grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                     # Media phrase
    RELATION: {<V.*> <DT>?<JJ>*<NN.*>+}            # Relation phrase
    ENTITY: {<NN.*>}                               # Entity phrase
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Print the result
print(chunked)
chunked.draw()  # (optional) visualize the chunk structure
