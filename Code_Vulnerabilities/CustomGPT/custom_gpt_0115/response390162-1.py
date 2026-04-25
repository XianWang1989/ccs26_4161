
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Example phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag
tokens = word_tokenize(phrase)
tagged = pos_tag(tokens)

# Define the grammar for cascading chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Apply the chunk parser
chunked = chunk_parser.parse(tagged)

# Display the result
print(chunked)

# Visualize the chunk tree (optional, requires `nltk` library graphics)
# chunked.draw()
