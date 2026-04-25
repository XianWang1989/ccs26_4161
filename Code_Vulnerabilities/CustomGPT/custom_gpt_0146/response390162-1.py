
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import RegexpParser

# Sample text
text = "Adventure movies between 2000 and 2015 featuring performances by Daniel Craig."

# Tokenize and POS tagging
tokens = word_tokenize(text)
tagged_tokens = pos_tag(tokens)

# Define your grammar for chunking
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                               # Media phrases
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}                     # Relations with verbs
  ENTITY: {<NN.*>}                                        # General entities 
  """

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Perform chunking
chunked = chunk_parser.parse(tagged_tokens)

# Show the chunked output
print(chunked)

# Pretty display of the chunks
chunked.draw()
