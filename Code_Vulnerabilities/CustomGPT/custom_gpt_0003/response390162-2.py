
import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

# Sample text
text = "adventure movies between 2000 and 2015 featuring performances by daniel craig"

# Tokenizing the text
tokens = word_tokenize(text)
# Part-of-speech tagging
tagged = pos_tag(tokens)

# Define the grammar
grammar = r"""
  MEDIA: {<DT>?<JJ>*<NN.*>+}                 
  RELATION: {<VB.*><DT>?<JJ>*<NN.*>+}       
  ENTITY: {<NN.*>}                           
"""

# Create the chunk parser
chunk_parser = RegexpParser(grammar)

# Chunk the tagged tokens
chunked = chunk_parser.parse(tagged)

# Print the chunked output
print(chunked)

# Visualize the structure
chunked.draw()
