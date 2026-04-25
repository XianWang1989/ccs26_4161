
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Example phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the phrase
tokens = word_tokenize(phrase)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                     # Media noun phrases
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}           # Relation involving verbs and noun phrases
  ENTITY: {<NN.*>}                               # Generic entities
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged)

# Print the chunked output
print(chunked)

# Optional: Draw the parse tree
chunked.draw()
