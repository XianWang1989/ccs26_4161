
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the text
tokens = word_tokenize(text)
tagged_tokens = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                     # Media titles
  RELATION: {<V.*>}{<DT>?<JJ>*<NN.*>+}          # Relations, e.g., 'featuring performances'
  ENTITY: {<NN.*>}                               # Entities
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunks = chunk_parser.parse(tagged_tokens)

# Display the chunk tree
print(chunks)

# Optionally draw the chunk tree (requires Tkinter)
# chunks.draw()
