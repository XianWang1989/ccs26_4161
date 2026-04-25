
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample sentence
sentence = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenize and POS tag the sentence
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Define the chunk grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                   # Media noun phrases
  RELATION: {<V.*><DT>?<JJ>*<NN.*>+}           # Relations with media
  ENTITY: {<NN.*>}                             # Entity phrases
  """

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged sentence
parsed_tree = chunk_parser.parse(tagged)

# Print the parsed tree
print(parsed_tree)

# Visualize the chunked structure
parsed_tree.draw()
