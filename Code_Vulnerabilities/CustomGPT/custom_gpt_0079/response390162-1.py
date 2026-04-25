
import nltk
from nltk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tagging
tokens = word_tokenize(phrase)
tagged = pos_tag(tokens)

# Define your grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                       # Media
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}               # Relation
  ENTITY: {<NN.*>}                                 # Entity
  """

# Initialize the chunk parser
chunk_parser = RegexpParser(grammar)

# Chunk the tagged tokens
chunked = chunk_parser.parse(tagged)

# Print the chunked tree
print(chunked)

# To visualize the chunk tree (optional)
chunked.draw()
