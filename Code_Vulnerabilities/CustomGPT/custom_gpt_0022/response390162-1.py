
import nltk
from nltk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Example phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
"""

# Create a parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Print the chunked output
print(chunked)

# Optionally draw the tree
chunked.draw()
