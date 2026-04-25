
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the text
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
    MEDIA: {<DT>?<JJ>*<NN.*>+}                     # Chunk sequences of DT, JJ, NN
    RELATION: {<V.*>}{<DT>?<JJ>*<NN.*>+}          # Chunk verbs followed by NP
    ENTITY: {<NN.*>}                               # Chunk Nouns
"""

# Create a chunk parser with the defined grammar
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
result = chunk_parser.parse(tagged)

# Print the resulting chunks
print(result)
result.draw()  # This will open a window to visualize the tree structure
