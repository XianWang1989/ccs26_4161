
import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenizing and tagging
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Defining the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}            # Media chunks
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}   # Relation chunks
  ENTITY: {<NN.*>}                       # Entity chunks
"""

# Creating the chunk parser
chunk_parser = RegexpParser(grammar)

# Parsing the tagged input
chunked = chunk_parser.parse(tagged)

# Displaying the chunks
print(chunked)

# Optional: Draw the chunk tree
chunked.draw()
