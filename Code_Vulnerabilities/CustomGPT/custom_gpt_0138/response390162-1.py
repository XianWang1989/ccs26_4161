
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Your sentence
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Define your grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}               # Define media
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}       # Define relations
  ENTITY: {<NN.*>}                          # Define entities
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged text
chunked = chunk_parser.parse(tagged)

# Draw the tree or extract chunks
print(chunked)  # Or use chunked.draw() to visualize
