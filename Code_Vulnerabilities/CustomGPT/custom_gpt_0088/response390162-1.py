
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the chunk grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                   # Chunk sequences of DT, JJ, NN
  RELATION: {<V.*>}{<DT>?<JJ>*<NN.*>+}        # Relation with verb followed by NP
  ENTITY: {<NN.*>}                             # Chunk nouns
"""

# Create a RegexpParser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
chunks = chunk_parser.parse(tagged)

# Show the results
print(chunks)
chunks.draw()  # Optional: To visualize the tree structure
