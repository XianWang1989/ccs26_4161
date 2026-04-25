
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample phrase
phrase = "adventure movies between 2000 and 2015 featuring performances by Daniel Craig"

# Tokenize and POS tagging
tokens = word_tokenize(phrase)
tagged_tokens = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                # Chunk sequences of DT, JJ, NN
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}       # Chunk verbs followed by MEDIA
  ENTITY: {<NN.*>}                           # Chunk nouns as ENTITY
  """

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged tokens
chunked = chunk_parser.parse(tagged_tokens)

# Print the result
print(chunked)

# Visualize the chunks (optional)
chunked.draw()
