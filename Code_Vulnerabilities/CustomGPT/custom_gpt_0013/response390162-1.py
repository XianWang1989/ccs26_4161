
import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Sample text
text = "Adventure movies between 2000 and 2015 featuring performances by Daniel Craig."

# Tokenizing and tagging
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}               # Media phrases
    RELATION: {<V.*>}{<DT>?<JJ>*<NN.*>+}     # Relations
    ENTITY: {<NN.*>}                         # Entity recognition
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged)

# Print the chunked output
print(chunked)

# If you want to visualize the tree structure
chunked.draw()
