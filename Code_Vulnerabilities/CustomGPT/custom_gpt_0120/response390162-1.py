
import nltk
from nltk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Example sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag
tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}             # Media chunk
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}    # Relation chunk
  ENTITY: {<NN.*>}                       # Entity chunk
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the POS tagged tokens
chunked_sentence = chunk_parser.parse(pos_tags)

# Print the chunked output
print(chunked_sentence)

# Draw the chunk tree (optional visualization)
chunked_sentence.draw()
