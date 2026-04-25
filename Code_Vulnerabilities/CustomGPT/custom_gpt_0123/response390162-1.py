
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample text
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                     # Chunk media phrases
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}             # Chunk relations
  ENTITY: {<NN.*>}                                # Chunk named entities
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
tree = chunk_parser.parse(tagged)

# Display the chunk tree
print(tree)

# Optionally, draw the tree
# tree.draw()
