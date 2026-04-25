
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define your grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                       # Media phrases
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}              # Relation phrases
  ENTITY: {<NN.*>}                                 # Entities
  CLAUSE: {<MEDIA><RELATION>}                      # Phrases containing MEDIA followed by RELATION
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Print the chunks
print(chunked)

# Optional: Draw the chunk tree
chunked.draw()
