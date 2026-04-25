
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and tag parts of speech
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                       # Media noun phrases
  RELATION: {<V.*>}{<DT>?<JJ>*<NN.*>+}             # Relations followed by noun phrases
  ENTITY: {<NN.*>}                                 # General entities
  """

# Create a chunk parser with the grammar
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
chunked = chunk_parser.parse(tagged)

# Display the result
print(chunked)

# Optionally, draw the chunks for visualization
chunked.draw()
