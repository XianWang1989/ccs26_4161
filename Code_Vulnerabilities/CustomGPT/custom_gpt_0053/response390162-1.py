
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}               # Media phrase
  RELATION: {<V.*>}{<DT>?<JJ>*<NN.*>+}     # Relation phrase
  ENTITY: {<NN.*>}                          # Entity chunk
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Display the chunked structure
print(chunked)

# Display tree
chunked.draw()
