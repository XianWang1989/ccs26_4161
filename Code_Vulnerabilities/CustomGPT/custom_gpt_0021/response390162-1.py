
import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenizing and tagging the phrase
tokens = word_tokenize(phrase)
tagged = pos_tag(tokens)

# Defining the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                    # Media Chunk
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}           # Relation Chunk
  ENTITY: {<NN.*>}                               # Entity Chunk
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Perform the chunking
result = chunk_parser.parse(tagged)

# Display the result
print(result)

# To visualize the chunk tree, you can use:
result.draw()
