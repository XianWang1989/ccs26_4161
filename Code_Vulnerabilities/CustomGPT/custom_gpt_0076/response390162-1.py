
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar with cascading rules
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                       # Media NPs
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}               # Relations followed by NPs
  ENTITY: {<NN.*>}                                 # Entities
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)
