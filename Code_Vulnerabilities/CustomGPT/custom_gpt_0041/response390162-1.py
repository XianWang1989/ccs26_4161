
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define your grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                   # Chunk media
  RELATION: {<V.*>}{<DT>?<JJ>*<NN.*>+}         # Chunk relations
  ENTITY: {<NN.*>}                             # Chunk entities
"""

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Visualize the chunked output
print(chunked)

# To specify specific words (like "directed" or "acted"), you can extend your grammar:
extended_grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}
  RELATION: {<VB.*>?<DT>?<JJ>*<NN.*>+}      # Adjustments to include specific verb forms
  ENTITY: {<NN.*>}
  SPECIFIC_RELATION: {<VB.*>(directed|acted)}
"""

# Create an extended chunk parser
extended_chunk_parser = RegexpParser(extended_grammar)

# Parse the tagged tokens with extended rules
extended_chunked = extended_chunk_parser.parse(tagged_tokens)

# Visualize the extended chunked output
print(extended_chunked)
