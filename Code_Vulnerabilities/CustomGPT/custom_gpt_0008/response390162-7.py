
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Define the input text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*>(<DT>?<JJ>*<NN.*>+)}
  ENTITY: {<NN.*>}
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)
tree = chunk_parser.parse(tagged)

# Print and visualize the chunk tree
print(tree)
tree.draw()
