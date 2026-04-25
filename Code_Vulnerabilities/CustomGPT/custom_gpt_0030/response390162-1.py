
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Define your grammar with nested structures
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Example phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the phrase
tokens = word_tokenize(phrase)
tagged = pos_tag(tokens)

# Parse the tagged tokens with the chunk parser
parsed_tree = chunk_parser.parse(tagged)

# Draw the resulting parse tree (optional)
parsed_tree.draw()

# Print the chunked structure
print(parsed_tree)
