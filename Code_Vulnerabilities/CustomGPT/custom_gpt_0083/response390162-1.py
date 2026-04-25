
import nltk
from nltk.chunk import RegexpParser
from nltk import pos_tag, word_tokenize

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig directed by aiden"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}  # Chunk sequences of DT, JJ, NN
  RELATION: {<VB.*> <DT>?<JJ>*<NN.*>+}  # Verbs followed by NPs
  ENTITY: {<NN.*>}          # General entity
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Apply the chunker to the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Print the chunks
print(chunked)

# To visualize, you may use:
chunked.draw()
