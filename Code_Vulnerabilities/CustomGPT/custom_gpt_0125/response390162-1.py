
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenizing and POS tagging
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                           # Chunk sequences of DT, JJ, NN
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}                 # Chunk verbs followed by DT, JJ, NN
  ENTITY: {<NN.*>}                                    # Chunk nouns
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged)

# Print the chunked result
print(chunked)

# To visualize the chunks
chunked.draw()
