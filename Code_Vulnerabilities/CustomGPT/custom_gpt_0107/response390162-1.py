
import nltk
from nltk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                # Media phrases
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}       # Relations involving verbs
  ENTITY: {<NN.*>}                          # Entities
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged)

# Print the chunked structure
print(chunked)

# Draw the tree for better visualization (optional)
chunked.draw()
