
import nltk
from nltk.chunk import RegexpParser
from nltk import pos_tag, word_tokenize

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(phrase)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                       # Media phrases
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}              # Relations like "directed" or "acted"
  ENTITY: {<NN.*>}                                 # Entities
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Chunk the tagged words
chunked = chunk_parser.parse(tagged)

# Display the results
print(chunked)

# Draw the chunk tree
chunked.draw()
