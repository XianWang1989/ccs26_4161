
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the chunk grammar with cascading rules
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                      # Chunk for MEDIA
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}              # Chunk for RELATION
  ENTITY: {<NN.*>}                                # Chunk for ENTITY
  """

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
chunked = chunk_parser.parse(tagged)

# Print the chunked structure
print(chunked)

# Optionally, visualize the chunked structure
chunked.draw()
