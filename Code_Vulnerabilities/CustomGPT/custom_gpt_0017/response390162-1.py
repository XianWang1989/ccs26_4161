
import nltk
from nltk import pos_tag, ne_chunk
from nltk.tokenize import word_tokenize
from nltk.chunk import RegexpParser

# Example sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                             # Media phrases like "adventure movies"
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}                     # Relation phrases like "featuring performances"
  ENTITY: {<NN.*>}                                       # Standalone entities like "daniel craig"
  """

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tags
chunked = chunk_parser.parse(tagged)

# Print the results
print(chunked)
chunked.draw()
