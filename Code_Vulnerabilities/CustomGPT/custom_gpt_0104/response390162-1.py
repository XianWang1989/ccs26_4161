
import nltk
from nltk import pos_tag
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize

# Sample sentence to be chunked
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig directed by some director"

# Tokenization and POS tagging
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar for your cascading chunker
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                       # Chunk for media types
  RELATION: {<V.*>}{<DT>?<JJ>*<NN.*>+}             # Chunk for relationships
  ENTITY: {<NN.*>}                                 # Chunk for entities
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Perform chunking
chunked_syntax = chunk_parser.parse(tagged)

# Print the chunked output
print(chunked_syntax)

# To visualize the chunked output (Make sure to have matplotlib installed)
# nltk.TreeView(chunked_syntax).draw()  # Uncomment if you want to visualize the tree
