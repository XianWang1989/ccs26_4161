
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenizing and POS tagging
tokens = word_tokenize(phrase)
tagged = pos_tag(tokens)

# Define the grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                     # Chunk sequences of DT, JJ, NN
  RELATION: {<V.*>{<DT>?<JJ>*<NN.*>+}}           # Chunk verbs followed by MEDIA
  ENTITY: {<NN.*>}                               # Chunk simple nouns
"""

# Create a RegexpParser using the defined grammar
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
result = chunk_parser.parse(tagged)

# Print the result
print(result)

# Optional: Draw the tree
result.draw()
