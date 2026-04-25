
import nltk
from nltk import pos_tag
from nltk import word_tokenize
from nltk.chunk import RegexpParser

# Example phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenizing and POS tagging
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Print the chunked result
print(chunked)

# Visualize the chunks using NLTK's tree display
chunked.draw()
