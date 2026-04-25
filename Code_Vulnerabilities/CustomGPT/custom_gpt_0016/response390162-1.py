
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define your grammar
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                       # Chunk media terms
    RELATION: {<V.*><DT>?<JJ>*<NN.*>+}                # Chunk relations with media
    ENTITY: {<NN.*>}                                  # Chunk entities
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged text
chunked = chunk_parser.parse(tagged)

# Show the chunked output
print(chunked)

# If you want to draw the tree (requires graphical backend)
chunked.draw()
