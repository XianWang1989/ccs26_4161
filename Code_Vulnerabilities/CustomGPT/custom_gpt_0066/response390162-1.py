
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)

# Define the grammar with cascading rules
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                                # Chunk for Media
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}                       # Chunk for Relation
  ENTITY: {<NN.*>}                                          # Chunk for Entity
  """

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Perform chunking
chunked = chunk_parser.parse(tagged_tokens)

# Show the chunked output
print(chunked)
