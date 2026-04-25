
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the text
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+</DT>}               # Chunk for media
  RELATION: {<V.*>}{<DT>?<JJ>*<NN.*>+}         # Chunk for relation
  ENTITY: {<NN.*>}                             # Chunk for entities
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged)

# Print the result
print(chunked)
chunked.draw()  # Optional: visualize the tree structure
