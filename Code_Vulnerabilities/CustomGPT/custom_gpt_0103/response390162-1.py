
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<V.*> <DT>?<JJ>*<NN.*>+}
  ENTITY: {<NN.*>}
  SPECIFIC: {<VB.*> <IN> <ENTITY>}  # For specific words like "directed", "acted"
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Apply the chunk parser to the tagged tokens
chunked = chunk_parser.parse(tagged)

# Display the chunked result
print(chunked)
