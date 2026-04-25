
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by Daniel Craig"

# Tokenize and POS tag
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define your grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                  # Media phrases
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}          # Relations with verbs followed by media
  ENTITY: {<NN.*>}                             # Entities (single nouns)
"""

# Create a RegexpParser
chunk_parser = RegexpParser(grammar)

# Parse the sentence
chunked = chunk_parser.parse(tagged)

# Print the chunked result
print(chunked)
chunked.draw()  # Visualize the chunking
